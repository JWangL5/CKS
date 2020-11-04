from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import notes, users, reviews, pictures
from django.db.models import Count

# Create your views here.


def index(request):
	mainhead = request.session.get("uhead", "pictures/toux.jpg")
	uid = request.session.get("userxh", "pictures/toux.jpg")

	lg = notes.objects.filter(ncolumn='TP')
	rw = notes.objects.filter(ncolumn='G')
	rb = notes.objects.all().order_by('-ngood')[0:5]

	# noteslst = notes.objects.all()
	return render(request, 'CKS.HTML', {"mainhead":mainhead,"lgnotes":lg,"rwnotes":rw,"rbnotes":rb,"uid":uid})


def mainother(request):
	return redirect('/')


def notecontent(request, id):
	mainhead = request.session.get("uhead", "pictures/toux.jpg")
	mainxh = request.session.get("userxh", "pictures/toux.jpg")
	# return HttpResponse(f"nid = {nid}")
	n = notes.objects.get(nid=id)
	nau = n.nauthor_id
	u = users.objects.get(uid=nau)
	img = u.uhead
	# print(img.url)
	# print(n.ncontent)
	
	rpsg = notes.objects.all()
	num_re = reviews.objects.filter(rreply_id=id).count()
	num_psg = notes.objects.filter(nauthor_id=id).count()
	dic = {
		"ntitle":n.ntitle,
		"nread":n.nread,
		"ncontent":n.ncontent,
		"ngood":n.ngood,
		"uname":u.uname,
		"uid2":u.uid2,
		"relatedpsg":rpsg[0:9],
		"num_re":num_re,
		"num_psg":num_psg,
		"num_read":n.nread,
		"nhead":img.url.split('/')[-1],
		"mainhead":mainhead,
		'xh':mainxh
	}
	return render(request, 'passage.html', dic)


def login(request):

	uxh = request.POST.get('user')
	pwd = request.POST.get('pwd')

	try:
		u = users.objects.get(uid2=uxh)
	except Exception as e:
		return HttpResponse("学号/密码错误")

	if pwd == u.upwd:
		# res = HttpResponse()
		request.session['uhead'] = u.uhead.url.split('/')[-1]
		request.session['userid'] = u.uid
		request.session['userxh'] = u.uid2
		# Redis的作用与Token
		# res.set_cookie('token', 'abdfjnjabfoabs;kfbas')
		mainhead = request.session.get("uhead", "pictures/toux.jpg")
		# request.session.set_expiry(10)
		# 默认半个月过期也还能接受
		return redirect('user/'+u.uid2)
	else:
		return HttpResponse("学号/密码错误")


def userspace(request, uid2):
	xh = request.session.get("userxh", "")
	if uid2 == xh:
		mainhead = request.session.get("uhead", "pictures/toux.jpg")
		return render(request, 'myspace.html', {"mainhead":mainhead})
	else:
		return HttpResponse("请先登陆")