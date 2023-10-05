const search = () => {
    const searchBox = document.getElementById("search-item").value.toUpperCase();
    const storyItems = document.getElementById("product-list");
    const product = storyItems.querySelectorAll(".product"); // ปรับให้เลือกรายการสินค้าภายใน storyItems

    for (var i = 0; i < product.length; i++) {
      let match = product[i].querySelector('h2 a'); // แก้ไขการค้นหารายการชื่อสินค้า
    
        if (match) {
            let textvalue = match.textContent || match.innerText;
    
            if (textvalue.toUpperCase().indexOf(searchBox) > -1) {
            product[i].style.display = "";
            } else {
            product[i].style.display = "none";
            }
        }
        }
    };
    
// function search() {
//     const searchInput = document.getElementById("search-item").value.toLowerCase();
//     const productNames = document.querySelectorAll(".product-name");

//     productNames.forEach(function (productName) {
//         const name = productName.textContent.toLowerCase();
//         const productListItem = productName.closest(".product-list");
//         if (name.includes(searchInput)) {
//             productListItem.style.display = "block";
//         } 
//         else {
//         productListItem.style.display = "none";
//         }
//     });
//     }
