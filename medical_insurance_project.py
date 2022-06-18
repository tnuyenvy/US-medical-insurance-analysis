#MEDICAL INSURANCE PROJECT
#given a raw dataset of patient infor and insurance cost

# Goal: 
# find average age of the patients
# return the number of males vs. females counted in the dataset
# organize into dictionaries
# insurance costs between smokers and non-smoker
# find unique geographical location of the patients

import csv
import re
# define empty list [empt_lst]
age=[]
sex=[]
bmi=[]
children=[]
smoker=[]
region=[]
charges=[]

#input: cvs file, output: list of each category with data [e.g Age=['23','24','25']]
def load_info(empt_lst,cvs_file,category):

    with open(cvs_file,newline='') as insurance_file:
        #convert to python with DictReader
        insurance_dict=csv.DictReader(insurance_file)
        for row in insurance_dict:
            empt_lst.append(row[category])
        return empt_lst


insurance_dir= "/Users/tranngocuyenvy/Desktop/python-portfolio-project-starter-files/insurance.csv"
load_info(age,insurance_dir,"age")
load_info(sex,insurance_dir,"sex")
load_info(bmi,insurance_dir,"bmi")
load_info(children,insurance_dir,"children")
load_info(smoker,insurance_dir,"smoker")
load_info(region,insurance_dir,"region")
load_info(charges,insurance_dir,"charges")


class PatientInfo:
    
    def __init__(self,age,sex,bmi,children,smoker,region,charges):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region
        self.charges=charges

    #return average age 
    def get_average_age(self):
        total=0
        for item in self.age:
            total+= int(item)
        return print("The average age is "+ str(round(total /len(self.age),2))+" years")

    #count gender
    def count_gender(self):
        total_female=0
        total_male=0
        for item in self.sex:
            if item=="female":
                total_female+=1
            else:
                total_male+=1
        return print("The female count is "+ str(total_female)), print("The male count is "+  str(total_male)) 
    
    #create a dictionary
    dict={}
    def create_dict(self):
        self.dict["age"]=self.age
        self.dict["sex"]=self.sex
        self.dict["bmi"]=self.bmi
        self.dict["children"]=self.children
        self.dict["smoker"]=self.smoker
        self.dict["region"]=self.region
        self.dict["charges"]=self.charges
        
        return self.dict

        
    # find the difference of average insurance costs between smokers and non-smoker
    def smoker_insurance_dif(self):
        smoker_charges=0
        non_smoker_charges=0
        for index in range(len(self.smoker)):
            if self.smoker[index]=="yes":
               smoker_charges+= float(self.charges[index])
            elif self.smoker[index]=="no":
                non_smoker_charges+=float(self.charges[index])
        aver_smoker=smoker_charges/len(smoker)
        aver_nonsmoker=non_smoker_charges/len(smoker)
        dif=aver_smoker-aver_nonsmoker
        return print("The smoker average insurance is {} and the non-smoker average insurance is {}. The difference between them is {}.".format(str(round(aver_smoker,2)),str(round(aver_nonsmoker,2)),str(round(dif,2))))
    
    #find unique regions in the list of regions
    def unique_geo(self):
        unique_lst=[]
        for item in self.region:
            if not item in unique_lst:
                unique_lst.append(item)
        return print(unique_lst)



patient_info= PatientInfo(age,sex,bmi,children,smoker,region,charges)
patient_info.get_average_age()
patient_info.count_gender()
patient_info.create_dict()
patient_info.smoker_insurance_dif()
patient_info.unique_geo()

#prints The average age is 39.21 years

