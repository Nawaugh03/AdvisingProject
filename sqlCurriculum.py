import mysql.connector

mydb = mysql.connector.connect(
                    host='localhost', 
                    user='root',      
                    password='1234',  
                    database='hawkdb'   
                    )
mycursor = mydb.cursor()

inputvalue="""INSERT INTO curriculums(courseID, course, number, title, credits) VALUES
                      (1001,'ENGL','203','Fundamentals of Contemporary Speech','3'),
                      (1002,'FREN','101','Fundamentals of French I','3'),
                      (1003,'FREN','102','Fundamentals of French II','3'),
                      (1004,'SPAN','101','Fundamentals of Spanish I','3'),
                      (1005,'SPAN','102','Fundamentals of Spanish II','3'),
                      (1006,'CHIN','101','Fundamentals of Chinese I','3'),
                      (1007,'CHIN','102','Fundamentals of Chinese II','3'),
                      (1008,'ARAB','101','Fundamentals of Arabic I','3'),
                      (1009,'ARAB','102','Fundamentals of Arabic II','3'),
                      (1010,'JAPN','101','Fundamentals of Japanese I','3'),
                      (1011,'JAPN','102','Fundamentals of Japanese II','3'),
                      (1012,'ECON','201','Principles of Economics(Macro)','3'),
                      (1013,'ECON','201H','Principles of Economics(Macro) Honors','3'),
                      (1014,'ECON','202','Principles of Economics(Micro)','3'),
                      (1015,'ECON','202H','Principles of Economics(Micro) Honors','3'),
                      (1016,'GEOG','101','The World Geography I','3'),
                      (1017,'GEOG','102','The World Geography II','3'),
                      (1018,'HIST','101','History of World Civilization I','3'),
                      (1019,'HIST','102','History of World Civilization II','3'),
                      (1020,'HIST','111H','History of World Civilization I Honors','3'),
                      (1021,'HIST','112H','History of World Civilization II Honors','3'),
                      (1022,'POLI','200','Introduction of American Government','3'),
                      (1023,'POLI','200H','Introduction of American Government Honors','3'),
                      (1024,'POLI','342','Urban Politics','3'),
                      (1025,'SOCI','101','Introduction to Sociology','3'),
                      (1026,'SOCI','111H','Introduction to Sociology Honors','3'),
                      (1027,'CRJS','101','Introduction to Criminal Justice','3'),
                      (1028,'HUEC','203','Human Development: A Lifespan Perspective','3'),
                      (1029,'HUEC','220','Perspectives on Aging','3'),
                      (1030,'HUEC','361','Contemporary Family Issues','3'),
                      (1031,'PSYC','101','Introduction to Psychology','3'),
                      (1032,'SOCI','201','Social Problems','3'),
                      (1033,'SOWK','200','Social Work','3'),
                      (1034,'SOCI','200H','Social Problems Honors','3'),
                      (1035,'BIOL','111','Principles of Biology I','3'),
                      (1036,'BIOL','113','Principles of Biology I Laboratory','1'),
                      (1037,'BIOL','112','Principles of Biology II','3'),
                      (1038,'BIOL','114','Principles of Biology II Laboratory','1'),
                      (1039,'CHEM','111','Principles of Chemistry I','3'),
                      (1040,'CHEM','113','Principles of Chemistry I Laboratory','1'),
                      (1041,'CHEM','112','Principles of Chemistry II','3'),
                      (1042,'CHEM','114','Principles of Chemistry II Laboratory','1'),
                      (1043,'MATH','112','Calculus I','4'),
                      (1044,'ENGL','101','Basic Composition I','3'),
                      (1045,'ENGL','101H','Basic Composition I(Honors)','3'),
                      (1046,'ENGL','102','Basic Composition II','3'),
                      (1047,'ENGL','102H','Basic Composition II','3'),
                      (1048,'ENGL','305/W','Twchnical Writing','3'),
                      (1049,'ENGL','310/W','Advanced Composition','3'),
                      (1050,'CSDP','100','Computer Science Orientation','1'),
                      (1051,'EXSC','111','Personalized Health Fitness','3'),
                      (1052,'CSDP','221','Introduction to Computer Programming','3'),
                       (1053,'CSDP','222','Advabced Programming','3'),
                       (1054,'CSDP','250','Data Structures','3'),
                       (1055,'CSDP','301','Computer Organization & Assembly Language Programming','3'),
                       (1056,'CSDP','305','Software Engineering I','3'),
                       (1057,'CSDP','332','Internet Programming','3'),
                       (1058,'CSDP','351','Computer Architecture','3'),
                       (1059,'CSDP','390','Social, Ethical and Legal Isssues in Computer Science','3'),
                       (1060,'CSDP','398','Computer Language Topics A: Java','3'),
                       (1061,'CSDP','399','Computer Langauge Topics B: UNIX','3'),
                       (1062,'CSDP','401','Operating Systems','3'),
                       (1063,'CSDP','402','Computer Networks','3'),
                       (1064,'CSDP','403','Computer Language Theory','3'),
                       (1065,'CSDP','404','Database Management Systems','3'),
                       (1066,'CSDP','450','Algorithms and Data Structures','3'),
                       (1067,'CSDP','490','Senior Design Project','3'),
                       (1068,'CSDP','341','Numerical Analysis I','3'),
                       (1069,'CSDP','395','Internship','3'),
                       (1070,'CSDP','405','Software Engineering II','3'),
                       (1071,'CSDP','431','Data Warehosuing and Data Mining','3'),
                       (1072,'CSDP','442','Numerical Analysis II','3'),
                       (1073,'CSDP','498','Selected Topics in Computer Science A','3'),
                       (1074,'CSDP','499','Selected Topics in Computer Science B','3'),
                       (1075,'MATH','350','Linear Programming','3'),
                       (1076,'MATH','211','Calculus II','4'),
                       (1077,'MATH','232','Introduction to Linear Algebra','3'),
                       (1078,'MATH','309','Introduction to Probability','3'),
                       (1079,'MATH','323','Introduction to Discrete Structures','3'),
                       (1080,'MATH','360','Statistics for Scientist','3'),
                       (1081,'ACCT','201','Introductory Financial Accounting','3'),
                       (1082,'ACCT','202','Introductory Corporate & Managerial Accounting/Hybrid','3'),
                       (1083,'MKTG','308','Principles of Marketing','3'),
                       (1084,'FINA','340','Financial Management','3'),
                       (1085,'BUAD','302','Management and Organizational Behavior','3'),
                       (1086,'MKTG','312','Sales Management','3'),
                       (1087,'MKTG','314','Retail Management','3'),
                       (1088,'MKTG','315','E-Commerce','3'),
                       (1089,'MKTG','401','Advertising Management','3'),
                       (1090,'MKTG','404','Consumer Behavior and Theory','3'),
                       (1091,'MKTG','410','Marketing Strategy and Policy','3'),
                       (1092,'FINA','341','Investment and Security Analysis','3'),
                       (1093,'FINA','440','Advanced Fiancial Management','3'),
                       (1094,'FINA','441','Insurance and Business Risks','3'),
                       (1095,'BUAD','242','The Lagal Enviornment for Business','3'),
                       (1096,'BUAD','303','Advanced Organizational Behavior','3'),
                       (1097,'BUAD','420','International Business','3');"""

#print(insert_Curriculum)
mycursor.execute(inputvalue)
mydb.commit()
#mycursor.execute("show tables;")
#myresult=mycursor.fetchall()
#print(myresult)

#print(type('hi'))
