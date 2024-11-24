from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Grade(models.Model):
    grade = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.grade

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
        ('male','Male'),
        ('female', 'Female')
    )

    name = models.CharField(max_length=200, null=True, verbose_name='Name * ')
    birthDate = models.DateTimeField(null=True, verbose_name='Date of Birth * ')
    birthPlace = models.CharField(max_length=200, null=True, verbose_name='Place of Birth * ')
    admission_level = models.ForeignKey(Grade, null=True, on_delete= models.SET_NULL, verbose_name='Admission Level * ')
    picture = models.ImageField(null=True, blank=True, verbose_name="Student's picture", upload_to='studentImages/')

    nationality = models.CharField(max_length=200, null=True, choices=COUNTRIES, default='Kenya', verbose_name='Nationality * ')
    town_name = models.CharField(max_length=200, null=True, verbose_name='Town Name * ')
    road_name = models.CharField(max_length=200, null=True, verbose_name='Road Name * ')
    previous_school = models.CharField(max_length=300, blank=True, null=True, verbose_name='Previous School * ')

    transport = models.CharField(max_length=200, null=True, choices=YESNO, verbose_name='Transport * ')
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
    registration_agent = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + ' | ' +self.admission_level.grade
    
    
