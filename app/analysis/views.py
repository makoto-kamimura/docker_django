from django.shortcuts import render

# view_main
def main(request):
    return render(request, 'analysis/main.html', {})