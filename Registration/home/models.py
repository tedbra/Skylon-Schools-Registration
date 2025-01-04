from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Grade(models.Model):
    grade = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.grade

class Payment(models.Model):
    payment_method = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.payment_method

class Student(models.Model):

    GRADE = (
        ('Reception','Reception'),
        ('PP1','PP1'),
        ('PP2','PP2'),
        ('Grade1','Grade 1'),
        ('Grade2','Grade 2'),
        ('Grade3','Grade 3'),
        ('Grade4','Grade 4'),
        ('Grade5','Grade 5'),
        ('Grade6','Grade 6'),
        ('Grade7','Grade 7'),
        ('Grade8','Grade 8'),
        ('Grade9','Grade 9')
    )

    COUNTRIES = (
    ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'),('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),('Armenia', 'Armenia'),('Australia', 'Australia'),('Austria', 'Austria'),('Azerbaijan', 'Azerbaijan'),('Bahamas', 'Bahamas'),('Bahrain', 'Bahrain'),('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),('Belarus', 'Belarus'),('Belgium', 'Belgium'),('Belize', 'Belize'),('Benin', 'Benin'),('Bhutan', 'Bhutan'),('Bolivia', 'Bolivia'),('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),('Brazil', 'Brazil'),('Brunei', 'Brunei'),('Bulgaria', 'Bulgaria'),('Burkina Faso', 'Burkina Faso'),('Burundi', 'Burundi'),('Cabo Verde', 'Cabo Verde'),('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),('Canada', 'Canada'),('Central African Republic', 'Central African Republic'),('Chad', 'Chad'),('Chile', 'Chile'),('China', 'China'),('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),('DR Congo', 'DR Congo'),('Congo Republic', 'Congo Republic'),('Costa Rica', 'Costa Rica'),('Croatia', 'Croatia'),('Cuba', 'Cuba'),
    ('Cyprus', 'Cyprus'),('Czech Republic', 'Czech Republic'),('Denmark', 'Denmark'),('Djibouti', 'Djibouti'),('Dominica', 'Dominica'),('Dominican Republic', 'Dominican Republic'),
    ('East Timor', 'East Timor'),('Ecuador', 'Ecuador'),('Egypt', 'Egypt'),('El Salvador', 'El Salvador'),('Equatorial Guinea', 'Equatorial Guinea'),('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),('Eswatini', 'Eswatini'),('Ethiopia', 'Ethiopia'),('Fiji', 'Fiji'),('Finland', 'Finland'),('France', 'France'),('Gabon', 'Gabon'),('Gambia', 'Gambia'),('Georgia', 'Georgia'),('Germany', 'Germany'),('Ghana', 'Ghana'),('Greece', 'Greece'),
    ('Grenada', 'Grenada'),('Guatemala', 'Guatemala'),('Guinea', 'Guinea'),('Guinea-Bissau', 'Guinea-Bissau'),('Guyana', 'Guyana'),('Haiti', 'Haiti'),('Honduras', 'Honduras'),('Hungary', 'Hungary'),('Iceland', 'Iceland'),('India', 'India'),('Indonesia', 'Indonesia'),('Iran', 'Iran'),('Iraq', 'Iraq'),('Ireland', 'Ireland'),('Italy', 'Italy'),('Ivory Coast', 'Ivory Coast'),('Jamaica', 'Jamaica'),('Japan', 'Japan'),('Jordan', 'Jordan'),('Kazakhstan', 'Kazakhstan'),('Kenya', 'Kenya'),('Kiribati', 'Kiribati'),('Korea, North', 'Korea, North'),('Korea, South', 'Korea, South'),('Kosovo', 'Kosovo'),('Kuwait', 'Kuwait'),('Kyrgyzstan', 'Kyrgyzstan'),('Laos', 'Laos'),('Latvia', 'Latvia'),('Lebanon', 'Lebanon'),('Lesotho', 'Lesotho'),('Liberia', 'Liberia'),('Libya', 'Libya'),('Liechtenstein', 'Liechtenstein'),('Lithuania', 'Lithuania'),('Luxembourg', 'Luxembourg'),('Madagascar', 'Madagascar'),('Malawi', 'Malawi'),('Malaysia', 'Malaysia'),('Maldives', 'Maldives'),('Mali', 'Mali'),('Malta', 'Malta'),('Marshall Islands', 'Marshall Islands'),('Mauritania', 'Mauritania'),('Mauritius', 'Mauritius'),('Mexico', 'Mexico'),('Micronesia', 'Micronesia'),('Moldova', 'Moldova'),('Monaco', 'Monaco'),('Mongolia', 'Mongolia'),('Montenegro', 'Montenegro'),('Morocco', 'Morocco'),('Mozambique', 'Mozambique'),('Myanmar', 'Myanmar'),('Namibia', 'Namibia'),('Nauru', 'Nauru'),('Nepal', 'Nepal'),('Netherlands', 'Netherlands'),('New Zealand', 'New Zealand'),('Nicaragua', 'Nicaragua'),('Niger', 'Niger'),('Nigeria', 'Nigeria'),('North Macedonia', 'North Macedonia'),('Norway', 'Norway'),('Oman', 'Oman'),('Pakistan', 'Pakistan'),('Palau', 'Palau'),('Palestine', 'Palestine'),('Panama', 'Panama'),('Papua New Guinea', 'Papua New Guinea'),('Paraguay', 'Paraguay'),('Peru', 'Peru'),('Philippines', 'Philippines'),('Poland', 'Poland'),('Portugal', 'Portugal'),('Qatar', 'Qatar'),('Romania', 'Romania'),('Russia', 'Russia'),('Rwanda', 'Rwanda'),('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),('Saint Lucia', 'Saint Lucia'),('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),('Samoa', 'Samoa'),('San Marino', 'San Marino'),('Sao Tome and Principe', 'Sao Tome and Principe'),('Saudi Arabia', 'Saudi Arabia'),('Senegal', 'Senegal'),('Serbia', 'Serbia'),('Seychelles', 'Seychelles'),('Sierra Leone', 'Sierra Leone'),('Singapore', 'Singapore'),('Slovakia', 'Slovakia'),('Slovenia', 'Slovenia'),('Solomon Islands', 'Solomon Islands'),('Somalia', 'Somalia'),('South Africa', 'South Africa'),('South Sudan', 'South Sudan'),('Spain', 'Spain'),('Sri Lanka', 'Sri Lanka'),('Sudan', 'Sudan'),('Suriname', 'Suriname'),('Sweden', 'Sweden'),('Switzerland', 'Switzerland'),('Syria', 'Syria'),('Taiwan', 'Taiwan'),('Tajikistan', 'Tajikistan'),('Tanzania', 'Tanzania'),('Thailand', 'Thailand'),('Togo', 'Togo'),('Tonga', 'Tonga'),('Trinidad and Tobago', 'Trinidad and Tobago'),('Tunisia', 'Tunisia'),('Turkey', 'Turkey'),('Turkmenistan', 'Turkmenistan'),('Tuvalu', 'Tuvalu'),('Uganda', 'Uganda'),('Ukraine', 'Ukraine'),('United Arab Emirates', 'United Arab Emirates'),('United Kingdom', 'United Kingdom'),('United States', 'United States'),('Uruguay', 'Uruguay'),('Uzbekistan', 'Uzbekistan'),('Vanuatu', 'Vanuatu'),('Vatican City', 'Vatican City'),('Venezuela', 'Venezuela'),('Vietnam', 'Vietnam'),('Yemen', 'Yemen'),('Zambia', 'Zambia'),('Zimbabwe', 'Zimbabwe')
    )

    COUNTRY = (
        ('Kenya','Kenya'),
        ('Uganda','Uganda'),
        ('Tanzania','Tanzania'),
        ('Rwanda','Rwanda'),
        ('Somalia','Somalia'),
        ('DR Congo','DR Congo'),
        ('Burundi','Burundi'),
        ('South Sudan','South Sudan'),
        ('Cameroon','Cameroon'),
        ('Nigeria','Nigeria'),
        ('Ghana','Ghana'),
        ('Other Eastern Africa','Other Estern Africa'),
        ('Central Africa','Central Africa'),
        ('Western Africa','Western Africa'),
        ('Southern Africa','Southern Africa'),
        ('Northern Africa','Northern Africa'),
        ('Europe','Europe'),
        ('Nigeria','Nigeria'),
        ('Ghana','Ghana'),
        ('Cameroon','Cameroon'),
        ('Nigeria','Nigeria'),
        ('Ghana','Ghana')
    )

    YESNO = (
        ('yes','YES'),
        ('no', 'NO')
    )

    GENDER= (
        ('girl','Boy'),
        ('boy', 'Girl')
    )

    PAYMENT_METHOD= (
        ('MPESA','MPESA'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Other', 'Other')
    )

    TERM = (
        ('Term 1','Term 1'),
        ('Term 2','Term 2'),
        ('Term 3','Term 3')
    )
    #system_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, verbose_name='Name * ')    
    birthDate = models.DateTimeField(null=True, verbose_name='Date of Birth * ')
    birthPlace = models.CharField(max_length=200, null=True, verbose_name='Place of Birth * ')
    gender = models.CharField(max_length=200, null=True, choices=GENDER, default="Girl", blank=True, verbose_name='Gender * ')
    admission_level = models.ForeignKey(Grade, null=True, on_delete= models.SET_NULL, verbose_name='Admission Level * ')
    picture = models.ImageField(null=True, blank=True, verbose_name="Student's picture", upload_to='studentImages/')
    nationality = models.CharField(max_length=200, null=True, choices=COUNTRIES, default='Kenya', verbose_name='Nationality * ')
    town_name = models.CharField(max_length=200, null=True, verbose_name='Town Name * ')
    road_name = models.CharField(max_length=200, null=True, verbose_name='Road Name * ')
    city_name = models.CharField(max_length=200, null=True, blank=True, default="Nairobi", verbose_name='City Name ')
    previous_school = models.CharField(max_length=300, blank=True, null=True, verbose_name='Previous School ')
    transport = models.CharField(max_length=200, null=True, choices=YESNO, default="No",verbose_name='Transport * ')
    optional_services_required_for_your_child = RichTextField(config_name='default',null=True, blank=True)
    #option_services = models.TextField(null=True, blank=True)

    emergency_contact = models.CharField(max_length=30, null=True, verbose_name="Primary Phone Number * ")
    mother_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Mother's Name")
    mother_phone = models.CharField(max_length=30, null=True, blank=True,verbose_name="Mother's Phone Number")
    father_name = models.CharField(max_length=200, null=True, blank=True,verbose_name="Father's Name")
    father_phone = models.CharField(max_length=30, null=True, blank=True,verbose_name="Father's Phone Number")
    guardian_name = models.CharField(max_length=200, null=True, blank=True,verbose_name="Guardian's Name")
    guardian_phone = models.CharField(max_length=30, null=True, blank=True,verbose_name="Guardian's Phone Number")

    date_added = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    term = models.CharField(max_length=200, null=True, choices=TERM, default="Term 1", blank=True, verbose_name='Term * ')
    payment = models.IntegerField(default=0,blank=True, verbose_name='Payment in Ksh')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD, null=True, blank=True, default = 'MPESA',verbose_name='Payment Method')
    reference = models.CharField(max_length=200, null=True, blank=True, verbose_name='Reference ')

    
    payment_history = models.TextField(blank=True)
    payment_baba = RichTextField(config_name='default', blank=True)
    student_ID = models.CharField(max_length=10, null=True, blank=True, verbose_name='Student ID')

    #staff_agent = models.CharField(max_length=100, null=True, blank=True, verbose_name='Registration Staff')    
    registration_agent = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Registration Staff')    

    def __str__(self):
        return self.name + ' | ' +self.admission_level.grade

    # def get_absolute_url(self):
    #     #return reverse('home')
    #     return reverse('student-detail', kwargs={'pk':self.id})    

    def para(self, *args, **kwargs):

        num_list = []
        current_date = datetime.now()

        print("What is in Payment History" + str(self.registration_agent))

        num_list.append('--' + str(current_date))
        num_list.append(' Updated by: '+ str(self.registration_agent))

        if self.payment:            
            num_list.append(' Amount: '+ str(self.payment))
            num_list.append(' Paid via: '+ str(self.payment_method))
            num_list.append(' Reference: '+ str(self.reference))
            num_list.append(' For: '+ str(self.term))
        else:
            num_list.append('No PAYMENT WAS DONE')
        
            
        new_entry = ','.join(map(str, num_list))
        new_entry_baba = '<p>' + new_entry + '</p>'

        self.payment_history = new_entry
        self.payment_baba = new_entry_baba

        self.payment = 0
        self.date_updated = current_date  

        super(Student, self).save(*args, **kwargs)
      

        if self.student_ID:
            print('ID OF Student Already Exist = ' + self.student_ID)
        else:
            date_de_merde = str(current_date)
            self.student_ID = 'SK'+ date_de_merde[2:4] + str(self.id).zfill(4)
            print('********* THE FOREIGN ID IS : ' + str(self.id))
            print("Why is it going here when there is data in payment history")

        super(Student, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     # Append a new number (for example, a random number) when the model is updated
        
    #     # Convert the existing string to a list
    #     if self.payment_history:
    #         num_list = [int(num) for num in self.payment_history.split(',')]
    #     else:
    #         num_list = []

    #     # Append the new number
    #     num_list.append(self.payment)

    #     # Convert the list back to a comma-separated string
    #     self.payment_history = ','.join(map(str, num_list))

    #     # Call the original save method
    #     super(Student, self).save(*args, **kwargs)










    
    
