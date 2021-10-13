from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '60900',
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни!'
             },
            {'name': 'Синяя куртка The North Face',
             'price': '23725',
             'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель!'
             },
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3390',
             'about': 'Материал с плюшевой текстурой. Удобный и мягкий!'
             },
        ],
    }
    return render(request, 'products/products.html', context)


def test(request):
    context = {
        'title': 'GeekShop test',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6090',
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': '23725',
             'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3390',
             'about': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
        ]
    }
    return render(request, 'products/test.html', context)





