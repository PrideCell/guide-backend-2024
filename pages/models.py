
from .choices import no_members_choices
from django.db import models
from cloudinary.models import CloudinaryField
from storages.backends.s3boto3 import S3Boto3Storage
from guide_project.storages_backends import MediaStorage
from .choices import type_choices
import os

# Create your models here.


def guide_directory_path(instance, filename):
    # Will be Uploaded to guide-images/<name>/<filename>
    return 'guide-images/{0}/{1}'.format(instance, filename)


def credit_directory_path(instance, filename):
    # Will be Uploaded to guide-images/<name>/<filename>
    return 'credit-images/{0}/{1}'.format(instance, filename)


class Guide(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(default=1)
    serial_no = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=100)
    domain_1 = models.CharField(max_length=200)
    domain_2 = models.CharField(max_length=200, blank=True, null=True)
    domain_3 = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    myImage = CloudinaryField('image')
    # myImage = models.ImageField(upload_to=guide_directory_path)
    # myImage = models.CharField(max_length=255)
    vacancy = models.IntegerField(default=7)

    def __str__(self):
        if self.name:
            return self.name
        


def user_directory_path(instance, filename):
    '''
    Instance is the value returned by __str__(self) which is teamID in this case
    So, instance = teamID
    As a result we can generate the path for each team using the return statement
    The instance and filename will be sent by FileField when this function in upload_to parameter!
    '''
    # Will be Uploaded to documents/<teamID>/<filename>
    return 'documents/{0}/{1}'.format(instance, filename)


def app_instance_path(instance, filename):
    # Will be Uploaded to appvideo/<teamID>/<filename>
    return os.path.join('app_based/{0}/{1}'.format(instance, filename))


def product_instance_path(instance, filename):
    # Will be Uploaded to productvideo/<teamID>/<filename>
    return os.path.join('product_based/{0}/{1}'.format(instance, filename))


class Team(models.Model):
    teamID = models.CharField(max_length=10)
    project_name = models.CharField(max_length=500)
    project_domain = models.CharField(max_length=100, null=True)
    project_description = models.TextField(null=True)
    no_of_members = models.CharField(
        max_length=10,
        choices=no_members_choices,
        default='1'
    )

    reg_no_1 = models.BigIntegerField()
    student_1_name = models.CharField(max_length=100)
    student_1_email = models.CharField(max_length=100)
    student_1_no = models.BigIntegerField()

    reg_no_2 = models.BigIntegerField(blank=True, null=True)
    student_2_name = models.CharField(max_length=100, blank=True, null=True)
    student_2_email = models.CharField(max_length=100, blank=True, null=True)
    student_2_no = models.BigIntegerField(blank=True, null=True)

    document = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)
    ppt = models.FileField(upload_to=user_directory_path,
                           null=True, blank=True)
    rs_paper = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)

    guide_form = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)

    app_video = models.FileField(
        upload_to=app_instance_path, null=True, blank=True)

    product_video = models.FileField(
        upload_to=product_instance_path, null=True, blank=True)

    profile_approved = models.BooleanField(default=False)
    guide_approved = models.BooleanField(default=False)
    rs_paper_approved = models.BooleanField(default=False)
    docs_approved = models.BooleanField(default=False)
    ppt_approved = models.BooleanField(default=False)
    guide = models.CharField(
        max_length=100)

    guide_email = models.CharField(max_length=100)

    review_2_marks = models.IntegerField(default=10)
    review_3_marks = models.IntegerField(default=10)

    student_1_marks = models.IntegerField(default=0)
    student_2_marks = models.IntegerField(default=0)

    communicated = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    payment_done = models.BooleanField(default=False)

    type = models.CharField(
        max_length=200, choices=type_choices, default=type_choices[0])

    def __str__(self):
        return self.teamID


class Temp_Team(models.Model):
    teamID = models.CharField(max_length=100, default='CSE')
    project_name = models.CharField(max_length=100)
    project_domain = models.CharField(max_length=100)
    project_description = models.TextField()
    no_of_members = models.CharField(
        max_length=10, choices=no_members_choices, default='1')

    reg_no_1 = models.BigIntegerField()
    student_1_name = models.CharField(max_length=100)
    student_1_email = models.CharField(max_length=100)
    student_1_no = models.BigIntegerField()

    reg_no_2 = models.BigIntegerField(blank=True, null=True)
    student_2_name = models.CharField(max_length=100, blank=True, null=True)
    student_2_email = models.CharField(max_length=100, blank=True, null=True)
    student_2_no = models.BigIntegerField(blank=True, null=True)

    guide_email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.project_name + ' ' + self.student_1_name + ' Added Sucessfully.'


class Otp(models.Model):
    user_email = models.CharField(max_length=100)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.user_email


class Otp_Two(models.Model):
    user_email = models.CharField(max_length=100)
    temp_email = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.user_email


class Temp_User(models.Model):
    user_email = models.EmailField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user_email


class Credit(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    img = CloudinaryField('image')

    def __str__(self):
        return self.name
