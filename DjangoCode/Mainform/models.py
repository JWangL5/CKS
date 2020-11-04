from django.db import models


# Create your models here.
class users(models.Model):
    uid = models.AutoField(primary_key=True)
    uid2 = models.CharField("学号", max_length=13, unique=True)
    uname = models.CharField("姓名", max_length=20)
    uintro = models.TextField("介绍", max_length=400)
    usign_datetime = models.DateTimeField("注册时间", auto_now_add=True)
    upsg_count = models.IntegerField("文章数量")  # default=0
    ucolumn = models.CharField("喜欢的领域", max_length=2)
    upwd = models.CharField("密码", max_length=20)
    uhead = models.ImageField("头像", upload_to="static/uhead/")

    def __str__(self):
        return f"{self.uid}-{self.uname}({self.uid2})"


class notes(models.Model):
    ntitle = models.CharField("标题", max_length=100)
    ncontent = models.TextField()  
    # 这里设置了允许Null，视图添加时请务必排查非空
    nauthor = models.ForeignKey('users', null=True,on_delete=models.SET_NULL) 
    ndatetime = models.DateTimeField("发布时间", auto_now=True)
    ncolumn = models.CharField("栏目", max_length=4)
    nid=models.AutoField("文章编号", primary_key=True)
    ngood = models.IntegerField("点赞量")
    nread = models.IntegerField("阅读量")


class reviews(models.Model):
    rauthor = models.ForeignKey('users', on_delete=models.CASCADE)
    rid=models.AutoField(primary_key=True)
    rcontent = models.TextField()
    rreply = models.ForeignKey('notes', on_delete=models.CASCADE)
    rgood = models.IntegerField()
    rdatetime = models.DateTimeField(auto_now=True)


class pictures(models.Model):
    pid = models.AutoField(primary_key=True)
    pfile = models.ImageField(upload_to="static/image/")
    pdatetime = models.DateTimeField()
    ppsg = models.ForeignKey('notes', on_delete=models.CASCADE)
