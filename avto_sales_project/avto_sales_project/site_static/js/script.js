// FAQ аккордеон
document.addEventListener('DOMContentLoaded', function() {
    const faqHeaders = document.querySelectorAll('.faq-header');
    
    faqHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const body = this.nextElementSibling;
            const icon = this.querySelector('i');
            
            // Проверяем, открыт ли текущий элемент
            const isOpen = body.classList.contains('show');
            
            if (isOpen) {
                // Закрываем текущий элемент
                body.classList.remove('show');
                if (icon) {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            } else {
                // Сначала закрываем все остальные элементы
                document.querySelectorAll('.faq-body').forEach(item => {
                    item.classList.remove('show');
                });
                
                document.querySelectorAll('.faq-header i').forEach(iconEl => {
                    iconEl.classList.remove('fa-chevron-up');
                    iconEl.classList.add('fa-chevron-down');
                });
                
                // Открываем текущий элемент
                body.classList.add('show');
                if (icon) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                }
            }
        });
    });

    // Галерея автомобилей
    const galleryThumbs = document.querySelectorAll('.gallery-thumb');
    const mainImage = document.getElementById('mainImage');
    
    galleryThumbs.forEach(thumb => {
        thumb.addEventListener('click', function() {
            // Удаляем активный класс у всех
            galleryThumbs.forEach(t => t.classList.remove('active'));
            
            // Добавляем активный класс текущему
            this.classList.add('active');
            
            // Меняем главное изображение
            if (mainImage) {
                mainImage.src = this.src;
            }
        });
    });

    // Плавное появление элементов при скролле
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.car-card, .advantage-item, .review-card').forEach(el => {
        observer.observe(el);
    });

    // Маска для телефона
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/[^\d\+\-\(\)\s]/g, '');
        });
    });
});
