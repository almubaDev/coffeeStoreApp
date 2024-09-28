document.addEventListener('DOMContentLoaded', function () {
        
    document.getElementById('product_search').addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase(); 
        const products = document.querySelectorAll('.product_card_manager');

        products.forEach(function(product) {
            const productName = product.querySelector('p').textContent.toLowerCase(); 

            if (productName.includes(searchTerm)) {
                product.style.display = 'block'; 
            } else {
                product.style.display = 'none'; 
            }
        });
    });
});

