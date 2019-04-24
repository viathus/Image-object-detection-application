from firebase import firebase
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from PIL.ImageQt import ImageQt
import cv2
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from userprofile import User
from testWidget import test_widget
from design import Ui_MainWindow
import threading
import time
from validate_email import validate_email
import re
from google.cloud import storage
import urllib.request
from PyQt5.QtWidgets import qApp
from utils import testdetection as vis_util
from time import gmtime, strftime
import datetime


#Creates connections to firebase
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./pythonapplication-15b3ad1dd76b.json"
firebase = firebase.FirebaseApplication('https://pythonapplication-aa823.firebaseio.com/',None)
client = storage.Client()
bucket = client.get_bucket('pythonapplication-aa823.appspot.com')



item = None #useritem
userID = None #unique user id to identify in firebase
current_user = None #the current user
answer = None #to check if we retrieve anything from firebase
fname= None #file name for image
f1= None #file output location
flag = True #flag to stop thread
fvideoname = None #video name

#Options to limit GPU uses
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
#
#LOADING IN MODEL
#
PATH_TO_MODEL = './Model/smoking_model.pb'
#Create Tensorflow graph which will allow us to reepesent units of computation and units of data that flow between operations
detection_graph = tf.Graph() #creates default graph
with detection_graph.as_default(): #allows us to define operations and tensors in detection graph
    od_graph_def = tf.GraphDef() #serialized version of graph, allows us to print, store or restore a graph
    with tf.gfile.GFile(PATH_TO_MODEL, 'rb') as fid: #Reads path to model saves it
        od_graph_def.ParseFromString(fid.read()) #Used saved model and convert it to the serialized version of graph.
        tf.import_graph_def(od_graph_def, name='') #import serialized graph and use it as a session

    sess = tf.Session(graph=detection_graph,config=config) #use graph and save it in a sess, so it can be called whenever needed

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0') #Get input image field
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0') #Get detection boxes field
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0') #Get detection scores field
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0') #Get detection classes field
num_detections = detection_graph.get_tensor_by_name('num_detections:0') #Get number of detections field


#Creates UI and sets up connections for buttons
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LoginButton.clicked.connect(self.login)
        self.ui.imagedetectbtn.clicked.connect(self.DetectImage)
        self.ui.openFilebtn.clicked.connect(self.openFile)
        self.ui.setPathbtn.clicked.connect(self.outputFile)

        self.ui.detectimage.clicked.connect(self.switchImageWidget)
        self.ui.detectvideo.clicked.connect(self.switchVideoWidget)
        self.ui.webcamDetect.clicked.connect(self.switchWebcamWidget)
        self.ui.usernotifications.clicked.connect(self.switchNotificationsWidget)
        self.ui.userSettings.clicked.connect(self.switchSettingsWidget)
        self.ui.logout.clicked.connect(self.switchLoginWidget)
        self.ui.signbtn.clicked.connect(self.switchSignupWidget)
        self.ui.createAccountbtn.clicked.connect(self.signup)
        self.ui.changeUserInfobtn.clicked.connect(self.switchUserInfoWidget)
        self.ui.Changepasswordbtn.clicked.connect(self.switchPasswordWidget)
        self.ui.saveuserinfobtn.clicked.connect(self.saveUserInfo)
        self.ui.savenewpasswordbtn.clicked.connect(self.saveNewPassword)
        self.ui.detectCamera.clicked.connect(self.detectCameraIP)
        self.ui.backToNotification.clicked.connect(self.switchNotificationsWidget)
        self.ui.filterbtn.clicked.connect(self.filterValues)
        self.ui.detectCamera_2.clicked.connect(self.detectVideo)
        self.ui.openFilebtn_2.clicked.connect(self.openVideoFile)
        self.ui.homebutton.clicked.connect(self.switchHomeWidget)
        #Create event for notification so user can delete or save
        self.ui.listWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.listWidget_2.customContextMenuRequested.connect(self.rightClickFunction)
        self.customMenu = QtWidgets.QMenu('Menu', self.ui.listWidget_2)
        self.customMenu.addAction(QtGui.QIcon('images/resize.png'), "Enlarge", self.enlargeImage)
        self.customMenu.addAction(QtGui.QIcon('images/save.png'), "Save", self.saveFunction)
        self.customMenu.addAction(QtGui.QIcon('images/delete.png'), "Delete", self.deleteFunction)


        #Filter
    def filterValues(self):
        #Array containing checkbox values
        Detection_type = []
        if self.ui.checkBox.isChecked():
            Detection_type.append("image")
        if self.ui.checkBox_2.isChecked():
            Detection_type.append("video")
        if self.ui.checkBox_3.isChecked():
            Detection_type.append("webcam")

        #Get date from user input and rearrange format
        date1 = datetime.datetime.strptime(str(self.ui.dateEdit_2.date().toPyDate()), '%Y-%m-%d').strftime('%d-%m-%Y')
        date2 = datetime.datetime.strptime(str(self.ui.dateEdit_3.date().toPyDate()), '%Y-%m-%d').strftime('%d-%m-%Y')

        #Go through each widget and filter it depending on what the user has picked
        for row in range(self.ui.listWidget_2.count()):
            index = self.ui.listWidget_2.item(row)
            widget = self.ui.listWidget_2.itemWidget(index)
            if self.filter(Detection_type, date1,date2,5,5,widget):
                index.setHidden(False)
            else:
                index.setHidden(True)




    #Filter if statements checks certain conditiions
    def filter(self, detection_types, date1, date2, time1, time2, widget):
        date_check = widget.customWidgetDate.text().replace("Date: ", "")
        type_check = widget.customWidgetType.text().replace("Detection: ", "")

        myDate = datetime.datetime.strptime(date_check,'%d-%m-%Y')
        userDate1 = datetime.datetime.strptime(date1,'%d-%m-%Y')
        userDate2 = datetime.datetime.strptime(date2,'%d-%m-%Y')
        default_date = datetime.datetime.strptime("01-01-2000",'%d-%m-%Y')

        #Order date so it doesnt matter which way user enters date
        if userDate1 != default_date and userDate2 != default_date:
            if userDate1 > userDate2:
                temp = userDate1
                userDate1 = userDate2
                userDate2 = temp


    
        #Filter
        #
        #Simple filter with IF statements to check if widget has the thing we are looking for if so filter accordingly
        #
        if len(detection_types) == 0:
            if default_date == userDate1 and default_date != userDate2:
                if userDate2 == myDate:
                    return True
                else:
                    return False
            elif default_date != userDate1 and default_date == userDate2:
                if userDate1 == myDate:
                    return True
                else:
                    return False
            elif userDate1 != default_date and userDate2 != default_date:
                if userDate1 <= myDate and userDate2 >= myDate:
                    return True
                else:
                    return False
        else:
            if default_date == userDate1 and default_date != userDate2:
                if userDate2 == myDate and type_check in detection_types:
                    return True
                else:
                    return False
            elif default_date != userDate1 and default_date == userDate2:
                if userDate1 == myDate and type_check in detection_types:
                    return True
                else:
                    return False
            elif userDate1 != default_date and userDate2 != default_date:
                if userDate1 <= myDate and userDate2 >= myDate and type_check in detection_types:
                    return True
                else:
                    return False
            elif userDate1 == default_date and userDate2 == default_date:
                if type_check in detection_types:
                    return True
                else:
                    return False
        return True






    #Enlarges image for detection image in notification
    def enlargeImage(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.largeImage)

        #Takes image and breaks the file name apart so it can be stored correctly
        widget = self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.currentItem())
        date = widget.customWidgetDate.text().replace("Date: ", "")
        time = widget.customWidgetScore.text().replace("Time: ", "")
        time = time.replace(":","-")
        type = widget.customWidgetType.text().replace("Detection: ", "")
        value = str(date+ " " +time + " " + type + ".jpg")


        #Get the user images and downloads them and displays it to the notifications
        imageBlob = bucket.blob(current_user + "/" + value)
        with urllib.request.urlopen(imageBlob.public_url) as url:
            s = url.read()
            pixmap1 = QtGui.QPixmap()
            pixmap1.loadFromData(s)
            pixmap = QtGui.QPixmap(pixmap1)
            self.ui.enlargeImagelabel.setPixmap(QtGui.QPixmap(pixmap))
            self.ui.enlargeImagelabel.setScaledContents(True)
            self.ui.enlargeImagelabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            self.ui.label_6.setText(widget.customWidgetDate.text())
            self.ui.label_32.setText(widget.customWidgetScore.text())
            self.ui.label_33.setText(widget.customWidgetType.text())


    #Allows you to save the images in notifications
    def saveFunction(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file != "":
            widget = self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.currentItem())
            date = widget.customWidgetDate.text().replace("Date: ", "")
            time = widget.customWidgetScore.text().replace("Time: ", "")
            time = time.replace(":","-")
            type = widget.customWidgetType.text().replace("Detection: ", "")
            value = str(date+ " " +time + " " + type + ".jpg")
            print(file+"/"+value)
            imageBlob = bucket.blob(current_user + "/" + value) #Get the users folder from database, and their images
            urllib.request.urlretrieve(imageBlob.public_url, file+"/"+value)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)

    #Allows you to delete notifications from your database
    def deleteFunction(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
        global item
        global firebase
        widget = self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.currentItem())
        date = widget.customWidgetDate.text().replace("Date: ", "")
        time = widget.customWidgetScore.text().replace("Time: ", "")
        time = time.replace(":","-")
        type = widget.customWidgetType.text().replace("Detection: ", "")
        value = str(date+ " " +time + " " + type + ".jpg")
        self.ui.listWidget_2.removeItemWidget(self.ui.listWidget_2.currentItem())
        self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(self.ui.listWidget_2.currentItem()))
        widget.deleteLater()
        key = None
        for k,v in answer["imagePaths"].items():
            if v == value:
                break
        firebase.delete("/users/" + userID + "/imagePaths/" + k, None)


        print("delete")

    #Creates right click options with enlarge, save, delete
    def rightClickFunction (self, event):
        global item
        index = self.ui.listWidget_2.indexAt(event)
        if not index.isValid():
            return
        item = self.ui.listWidget_2.indexAt(event)
        self.customMenu.popup(QtGui.QCursor.pos())



    #Saves new password
    def saveNewPassword(self):
        if self.ui.lineEdit_6.text() == answer["password"]:
            value = self.passwordValidation(self.ui.lineEdit_7.text())
            if "perfect" == value:
                if self.ui.lineEdit_7.text() == self.ui.lineEdit_8.text():
                    firebase.put('/users/'+ userID ,"password" , self.ui.lineEdit_7.text())
                    self.ui.errorlabel.setText("Updated password")
                else:
                    self.ui.errorlabel.setText("Passwords not the same")
            else:
                self.ui.errorlabel.setText(value)
        else:
            self.ui.errorlabel.setText("Current password is incorrect")


    #Saves user info
    def saveUserInfo(self):
        firebase.put('/users/'+ userID ,"firstName" , self.ui.lineEdit_3.text())
        firebase.put('/users/'+ userID ,"lastName" , self.ui.lineEdit_4.text())
        firebase.put('/users/'+ userID ,"email" , self.ui.lineEdit_5.text())


#These set up the switches between the different pages for the application
    def switchUserInfoWidget(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page)
        if answer is not None:
            self.ui.lineEdit_3.setText(answer["firstName"])
            self.ui.lineEdit_4.setText(answer["lastName"])
            self.ui.lineEdit_5.setText(answer["email"])
    def switchHomeWidget(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
    def switchPasswordWidget(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_2)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
    def switchImageWidget(self):
        self.ui.label_21.setText("")
        self.ui.fileLabel.setText("Open file path")
        self.ui.pathLabel.setText("set file path")
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.detect_image_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
    def switchWebcamWidget(self):
        self.ui.label_9.setText("")
        self.ui.cameraIP.setText("")
        self.ui.locationCamera.setText("")
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.detect_webcam_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
    def switchVideoWidget(self):
        self.ui.errorvideo.setText("")
        self.ui.fileLabel_2.setText("Open file path")
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.detect_video_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
    def switchSettingsWidget(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.setting_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_4)
    def switchNotificationsWidget(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.notification_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_5)
    def switchLoginWidget(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_5)
        self.ui.lineEdit_2.setText("")
        self.ui.listWidget_2.clear()
        self.ui.cameraIP.setText("")
        self.ui.label_17.setText("")
        self.ui.locationCamera.setText("")
        self.ui.fileLabel_2.setText("Open file path")
        self.ui.fileLabel.setText("Open file path")
        self.ui.pathLabel.setText("set file path")
        item = None
        userID = None
        current_user = None
        answer = None
        fname= None
        f1= None
        flag = True
        fvideoname = None


    #creates a thread which is consistenly checking users input and seeing if they have entered everything correctly
    def newFunc(self):
        global flag
        global firebase
        result = firebase.get('/users',None)
        time.sleep(2)
        while flag:
            #Check username field
            answer = None
            if self.ui.usernamelabel.text():
                if len(self.ui.usernamelabel.text()) >= 4:
                    answer  = next((item for item in result.values() if item["username"] == self.ui.usernamelabel.text()), None)
                    if answer is None:
                        self.ui.UsernameImg.setPixmap(QtGui.QPixmap("./images/greentick.png"))
                        self.ui.usernameBtn.setText("Perfect!")
                    else:
                        self.badUsernameField()
                        self.ui.usernameBtn.setText("Username already exists")
                else:
                    self.badUsernameField()
                    self.ui.usernameBtn.setText("Username must be at least 4 characters")
            else:
                self.badUsernameField()
                self.ui.usernameBtn.setText("Username must be unique")

            #Check email fields
            if self.ui.emaillabel.text():
                if validate_email(self.ui.emaillabel.text()):
                    self.goodEmailField()
                    self.ui.emailBtn.setText("Perfect!")
                else:
                    self.badEmailField()
                    self.ui.emailBtn.setText("Email must be valid")
            else:
                self.badEmailField()
                self.ui.emailBtn.setText("Email must be valid")

            #Check password fields
            if self.ui.passwordlabel.text():
                vald1 = self.passwordLengthValidation(self.ui.passwordlabel.text())
                vald3 = self.passwordNumberValidation(self.ui.passwordlabel.text())
                vald2 = self.passwordCapitalValidation(self.ui.passwordlabel.text())

                if vald1 == "perfect":
                    self.goodPasswordLengthField()
                    self.ui.passwordBtn.setText("Perfect!")
                else:
                    self.badPasswordLengthField()
                    self.ui.passwordBtn.setText("Password must be longer than 4 characters")

                if vald2 == "perfect":
                    self.goodPasswordCapitalField()
                    self.ui.passwordBtn_2.setText("Perfect!")
                else:
                    self.badPasswordCapitalField()
                    self.ui.passwordBtn_2.setText("Password must have a capital letter")

                if vald3 == "perfect":
                    self.goodPasswordNumberField()
                    self.ui.passwordBtn_3.setText("Perfect!")
                else:
                    self.badPasswordNumberField()
                    self.ui.passwordBtn_3.setText("Password must have a number")

                if self.ui.passwordlabel.text() == self.ui.passwordlabel2.text():
                    self.goodPasswordSameField()
                    self.ui.passwordBtn_4.setText("Perfect!")
                else:
                    self.badPasswordSameField()
                    self.ui.passwordBtn_4.setText("Passwords must be the same")
            else:
                self.badPasswordNumberField()
                self.badPasswordCapitalField()
                self.badPasswordLengthField()
                self.badPasswordSameField()
                self.ui.passwordBtn_3.setText("Password must have a number")
                self.ui.passwordBtn_2.setText("Password must have a capital letter")
                self.ui.passwordBtn.setText("Password must be longer than 4 characters")
                self.ui.passwordBtn_4.setText("Passwords must be the same")


            #     value = self.passwordValidation(self.ui.passwordlabel.text())
            #     if value == "perfect":
            #         if self.ui.passwordlabel2.text():
            #             if self.ui.passwordlabel.text() == self.ui.passwordlabel2.text():
            #                 self.goodPasswordField()
            #                 self.ui.passwordBtn.setText("Password is perfect!")
            #             else:
            #                 self.badPasswordField()
            #                 self.ui.passwordBtn.setText("Passwords must be the same")
            #         else:
            #             self.badPasswordField()
            #             self.ui.passwordBtn.setText("re-password field is empty!")
            #     else:
            #         self.badPasswordField()
            #         self.ui.passwordBtn.setText(value)
            # else:
            #     self.badPasswordField()
            #     self.ui.passwordBtn.setText("password field is empty!")




    def switchSignupWidget(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.label_17.setText("")
        threading.Thread(target=self.newFunc, daemon=True).start()


    def passwordLengthValidation(self, password):
        if len(password) <= 4:
            return "Make sure your password is at least 5 letters"
        else:
            return "perfect"

    def passwordNumberValidation(self, password):
        if re.search('[0-9]', password) is None:
            return "Make sure your password has a number in it"
        else:
            return "perfect"

    def passwordCapitalValidation(self, password):
        if re.search('[A-Z]', password) is None:
            return "Make sure your password has a capital letter in it"
        else:
            return "perfect"


    def goodUsernameField(self):
        self.ui.UsernameImg.setPixmap(QtGui.QPixmap("./images/greentick.png"))

    def badUsernameField(self):
        self.ui.UsernameImg.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))

    def goodEmailField(self):
        self.ui.emailImg.setPixmap(QtGui.QPixmap("./images/greentick.png"))

    def badEmailField(self):
        self.ui.emailImg.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))

    def goodPasswordLengthField(self):
        self.ui.passwordImg.setPixmap(QtGui.QPixmap("./images/greentick.png"))

    def badPasswordLengthField(self):
        self.ui.passwordImg.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))

    def goodPasswordCapitalField(self):
        self.ui.passwordImg_2.setPixmap(QtGui.QPixmap("./images/greentick.png"))

    def badPasswordCapitalField(self):
        self.ui.passwordImg_2.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))

    def goodPasswordNumberField(self):
        self.ui.passwordImg_3.setPixmap(QtGui.QPixmap("./images/greentick.png"))

    def badPasswordNumberField(self):
        self.ui.passwordImg_3.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))

    def goodPasswordSameField(self):
        self.ui.passwordImg_4.setPixmap(QtGui.QPixmap("./images/greentick.png"))

    def badPasswordSameField(self):
        self.ui.passwordImg_4.setPixmap(QtGui.QPixmap("./images/wrongcross.png"))

    def signup(self):
        global firebase
        global flag
        result = firebase.get('/users',None)
        firstname = self.ui.firstnamelabel.text()
        surname = self.ui.surnamelabel.text()
        email = self.ui.emaillabel.text()
        username = self.ui.usernamelabel.text()
        password = self.ui.passwordlabel.text()
        repassword = self.ui.passwordlabel2.text()

        #Quickly check which button is checked


        if "Perfect" in self.ui.emailBtn.text() and "Perfect" in self.ui.passwordBtn.text() and "Perfect" in self.ui.usernameBtn.text() and "Perfect" in self.ui.passwordBtn_2.text() and "Perfect" in self.ui.passwordBtn_3.text() and "Perfect" in self.ui.passwordBtn_4.text():
            flag = False

            user = User(firstname,surname, email, username, "Not specified", 5, password,[])
            result = firebase.post('/users',user.__dict__)

            self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)

        else:
            print("fix errors")





    #LETS THE USER Login
    def login(self):
        global answer
        global firebase
        global current_user
        global userID
        result = firebase.get('/users',None)
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        userID  = next((item for item in result if result[item]["username"] == username), None) #Get user ID
        answer  = next((item for item in result.values() if item["username"] == username), None) #Get user DATA

        if answer is None:
            self.ui.label_17.setText("User doesn't exist")
        else:
            if answer["password"] == password:
                current_user = answer["username"]
                #firebase.post('/users/'+ userID + '/imagePaths','C:/Users/abdsaam/Desktop/pythonapp/designs/images/greentick.png')
                self.ui.stackedWidget.setCurrentIndex(0)

                qApp.processEvents()
                if "imagePaths" in answer:
                    for x in answer["imagePaths"].values():
                        print(x)
                        imageBlob = bucket.blob(current_user + "/" + x) #Get the users folder from database, and their images
                        print(imageBlob.public_url)
                        with urllib.request.urlopen(imageBlob.public_url) as url:
                            s = url.read()
                            wid = test_widget()
                            wid.setImage(s)
                            values = x.split()


                            wid.setLabelDate(str("Date: " + values[0]))
                            wid.setLabelTime(str("Time: " + values[1].replace("-", ":")))
                            wid.setLabelType(str("Detection: " + values[2].replace(".jpg","")))
                            widgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget_2)
                            widgetItem.setSizeHint(wid.sizeHint())
                            self.ui.listWidget_2.addItem(widgetItem)
                            self.ui.listWidget_2.setItemWidget(widgetItem,wid)


                #imageBlob.upload_from_filename('C:/Users/abdsaam/Desktop/pythonapp/designs/images/greentick.png')

                # imageBlob = bucket.blob(self.ui.lineEdit.text()+"/")
                #print(imageBlob)
            else:
                self.ui.label_17.setText("Incorrect password")


    def DetectImage(self):
        self.ui.label_21.setText("Loading.... Application might freeze....")
        qApp.processEvents()
        global f1, fname


        image = cv2.imread(fname[0]) #get filename
        image_expanded = np.expand_dims(image, axis=0) #convert to numpy array

        #Saves model output into 4 values
        (boxes, scores, classes, num) = sess.run([detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded}) #uses model that was loaded in and feeds it a np array of the image we wish to have detected

        #Detect image
        vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            {1: {'name': 'smoker', 'id': 1}},
            use_normalized_coordinates=True,
            line_thickness=8,
            min_score_thresh=0.90)



        # selected_indices = tf.image.non_max_suppression(boxes[0], scores[0], 5, 0.5)
        # print(scores[0])
        # print(selected_indices)
        # print(selected_indices.get_shape().as_list())
        # selected_boxes = tf.gather(boxes, selected_indices)
        # print(selected_boxes)
        # print(selected_boxes.get_shape().as_list())
        # threshold = 0.5
        # height, width = image.shape[:2] #gets height and width of image
        # for x in selected_indices.get_shape().as_list():
        #     if x is None:
        #         ymin = boxes[0][0][0]*height
        #         xmin = boxes[0][0][1]*width
        #         ymax = boxes[0][0][2]*height
        #         xmax = boxes[0][0][3]*width
        #     else:
        #         ymin = boxes[0][x][0]*height
        #         xmin = boxes[0][x][1]*width
        #         ymax = boxes[0][x][2]*height
        #         xmax = boxes[0][x][3]*width
        #     cv2.rectangle(image, (int(xmin),int(ymin)), (int(xmax),int(ymax)),(0,255,0),5)

        #Get the date time and save it
        datetimevalue = strftime("%d-%m-%Y %H-%M-%S", gmtime())
        cv2.imwrite(f1 + "/" + datetimevalue + " " + "image" + ".jpg", image)
        pixmap = QtGui.QPixmap(f1 + "/" + datetimevalue + " " + "image" + ".jpg")
        scaled_pixmap = pixmap.scaled(500,500,QtCore.Qt.KeepAspectRatio)

        #Post the image to the database with the date and time
        self.ui.label_11.setPixmap(QtGui.QPixmap(scaled_pixmap))
        if self.ui.saveNotificationsImage.isChecked():
            value = datetimevalue + " " + "image" + ".jpg"
            firebase.post('/users/'+ userID + '/imagePaths', value)
            imageBlob = bucket.blob(current_user + "/" + value)
            path = f1 + "/" + datetimevalue + " " + "image" + ".jpg"
            imageBlob.upload_from_filename(path)
            self.newNotification(f1 + "/" + value, value)

        self.ui.label_21.setText("Done!")

    def newNotification(self, path, s):
        wid = test_widget()
        wid.setImage1(path)
        values = s.split()
        wid.setLabelDate(str("Date: " + values[0]))
        wid.setLabelTime(str("Time: " + values[1].replace("-", ":")))
        wid.setLabelType(str("Detection: " + values[2].replace(".jpg","")))
        widgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget_2)
        widgetItem.setSizeHint(wid.sizeHint())
        self.ui.listWidget_2.insertItem(0, widgetItem)
        self.ui.listWidget_2.setItemWidget(widgetItem,wid)

    def outputFile(self):
        global f1
        f1 = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        self.ui.pathLabel.setText(f1)

    def openFile(self):
        global fname
        fname = QFileDialog.getOpenFileName(None,'Open file','c:\\','Image files (*.jpg *.png)')
        pixmap = QtGui.QPixmap(fname[0])
        scaled_pixmap = pixmap.scaled(500,500,QtCore.Qt.KeepAspectRatio)
        self.ui.label_11.setPixmap(QtGui.QPixmap(scaled_pixmap))
        self.ui.fileLabel.setText(fname[0])

    def openVideoFile(self):
        global fvideoname
        fvideoname = QFileDialog.getOpenFileName(None,'Open file','c:\\','Video files (*.mp4 *.mov)')
        self.ui.fileLabel_2.setText(fvideoname[0])

    def detectVideo(self):
        global fvideoname
        self.ui.errorvideo.setText("Loading.... Application might freeze....")
        qApp.processEvents()
        video = cv2.VideoCapture(fvideoname[0])
        if video.isOpened():
            self.ui.errorvideo.setText("Done!")
            current_time = time.time()
            while(video.isOpened()):
                #Get frame and expand it so it can fed to tensorflow
                ret, frame = video.read()

                frame_expanded = np.expand_dims(frame, axis=0)
                # Perform the actual detection by running the model with the image as input
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: frame_expanded})

                #Draws bounding box around the detected part of the image #Helper code
                vis_util.visualize_boxes_and_labels_on_image_array(
                    frame,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    {1: {'name': 'smoker', 'id': 1}},
                    use_normalized_coordinates=True,
                    line_thickness=8,
                    min_score_thresh=0.90)

                #Show the detected image on the window
                cv2.imshow("video", frame)

                if scores[0][0]*100 > 90:
                    if self.thirty_timer(current_time):
                        current_time = time.time()
                        datetimevalue = strftime("%d-%m-%Y %H-%M-%S", gmtime())
                        cv2.imwrite("./videoimages" + "/" + datetimevalue + " " + "video" + ".jpg", frame)
                        if self.ui.saveNotificationsImage_3.isChecked():
                            value = datetimevalue + " " + "video" + ".jpg"
                            firebase.post('/users/'+ userID + '/imagePaths', value)
                            imageBlob = bucket.blob(current_user + "/" + value)
                            path = "./videoimages" + "/" + datetimevalue + " " + "video" + ".jpg"
                            imageBlob.upload_from_filename(path)
                            self.newNotification("./videoimages" + "/" + value, value)



                #Q or Esc to quit detecting webcam
                k = cv2.waitKey(1)
                if k == ord('q') or k == 27:
                    break
                if cv2.getWindowProperty("video",1) == -1:
                    break

            # Clean up
            video.release()
            cv2.destroyAllWindows()
        else:
            self.ui.errorvideo.setText("Error with video file")


    def thirty_timer(self,oldtime):
        return time.time() - oldtime >= 30

    def detectCameraIP(self):

        self.ui.label_9.setText("Loading.... Application might freeze....")
        qApp.processEvents()
        #Check if user is connecting to USB webcam or trying to connect to cameraIP address
        if self.ui.cameraIP.text().isdigit():
            cameraIPvalue = int(self.ui.cameraIP.text())
        else:
            cameraIPvalue = self.ui.cameraIP.text()

        video = cv2.VideoCapture(cameraIPvalue)
        video.set(3,1024)
        video.set(4,768)

        if video.isOpened():
            self.ui.label_9.setText("Done!")
            current_time = time.time()
            while(True):
                #Get frame and expand it so it can fed to tensorflow
                ret, frame = video.read()

                frame_expanded = np.expand_dims(frame, axis=0)
                # Perform the actual detection by running the model with the image as input
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: frame_expanded})

                #Draws bounding box around the detected part of the image #Helper code
                vis_util.visualize_boxes_and_labels_on_image_array(
                    frame,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    {1: {'name': 'smoker', 'id': 1}},
                    use_normalized_coordinates=True,
                    line_thickness=8,
                    min_score_thresh=0.90)

                #Show the detected image on the window
                cv2.imshow(self.ui.locationCamera.text(), frame)

                if scores[0][0]*100 > 90:
                    if self.thirty_timer(current_time):
                        current_time = time.time()
                        datetimevalue = strftime("%d-%m-%Y %H-%M-%S", gmtime())
                        cv2.imwrite("./webcamimages" + "/" + datetimevalue + " " + "webcam" + ".jpg", frame)
                        if self.ui.saveNotificationsImage_2.isChecked():
                            value = datetimevalue + " " + "webcam" + ".jpg"
                            firebase.post('/users/'+ userID + '/imagePaths', value)
                            imageBlob = bucket.blob(current_user + "/" + value)
                            path = "./webcamimages" + "/" + datetimevalue + " " + "webcam" + ".jpg"
                            imageBlob.upload_from_filename(path)
                            self.newNotification("./webcamimages" + "/" + value, value)



                #Q or Esc to quit detecting webcam
                k = cv2.waitKey(1)
                if k == ord('q') or k == 27:
                    break
                if cv2.getWindowProperty(self.ui.locationCamera.text(),1) == -1:
                    break

            # Clean up
            video.release()
            cv2.destroyAllWindows()
        else:
            self.ui.label_9.setText("Cannot find camera")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
exit(app.exec_())
