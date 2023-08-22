from django.shortcuts import render

# Create your views here.
async def home(request):
	ctx = {

	}
	return render(request, "index.html",ctx)