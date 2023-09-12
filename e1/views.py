from django.shortcuts import render,redirect
from e1.models import juguetes,electro,ropa


# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def elecData(request):
    electros = electro.objects.all()
    data = {
        'electro':electros,
    }
    return render(request, 'electro.html',data)

def jugarData(request):
    juguete = juguetes.objects.all()
    data = {
        'juguete':juguete,
        }
    return render(request, 'juguetes.html',data)

def ropaData(request):
    ropas = ropa.objects.all()
    data = {
        'ropa':ropas,
        }
    return render(request, 'ropa.html', data)

def agregar(request):
    Producto = request.POST['Producto']
    marca = request.POST['marca']
    precio = request.POST['precio']
    stock = request.POST['stock']
    try:
        foto = request.FILES['foto']
    except:
        foto = '/electronica/electro.png'

    Electronica = electro.objects.create(Producto=Producto,marca=marca,precio=precio,stock=stock,foto=foto)

    return redirect ('../index/electronica/')

def eliminar(request, id):
    muerte = electro.objects.get(id=id)
    muerte.delete()
    return redirect('../index/electronica/')

def editar(request, id):
    producto = electro.objects.get(id=id)
    data = {
        'electro':producto,
    }
    return render(request,'electroedit.html',data)

def editarElectro(request):
    id = request.POST['id']
    Producto = request.POST['Producto']
    marca = request.POST['marca']
    precio = request.POST['precio']
    stock = request.POST['stock']
    foto = request.FILES['foto']
    electronica = electro.objects.get(id=id)
    electronica.Producto = Producto
    electronica.marca = marca
    electronica.precio = precio
    electronica.stock = stock
    electronica.foto = foto
    electronica.save()
    return redirect('../index/electronica/')