//เปลี่ยน opcity จากก 0 เป็น 1
const openBtn = document.querySelector(".btn-review")
const closeBtn = document.querySelector(".close-btn")
const modalContainer = document.querySelector(".modal-container")

//ดักจับ event การกด click
openBtn.addEventListener("click",()=>{
    //เมื่อกด click ให้ add class show
    modalContainer.classList.add("show");
})

closeBtn.addEventListener("click",()=>{
    //เมื่อกด click ให้ add class show
    modalContainer.classList.remove("show");
})