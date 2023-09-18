/*.submit__btn == .btn-post*/

const submitBtn=document.querySelector('.btn-post');
const userName = document.querySelector("#name__star");
const comment=document.querySelector("#comment__star");
const likeIcon = document.querySelector(".heart__icon");
const count = document.querySelector(".count");
const commentCont = document.querySelector(".comments__containers");

likeIcon.addEventListener("click",likeVideo)
submitBtn.addEventListener("click",submitFeedback)

feedbackArr = []
let positiveFeedback = false
let likesCount = 0

//เก็บข้อมูลที่พิมพ์ในกล่อง
function submitFeedback(e){
    //get username
    const userForm = userName.value
    //get feedback
    const commentForm = comment.value
    if (userForm !== '' && commentForm !== '') {
        // สร้างข้อมูล feedback ใหม่
        const newFeedback = {
            "id": Math.floor((Math.random() * 1000) + 1),
            "userName": userForm,
            "userComment": commentForm,
            "typeOfFeedback": positiveFeedback
        };
    
        // เพิ่ม feedback ใหม่ลงใน feedbackArr
        feedbackArr.push(newFeedback);
    
        // หากเป็นการกด like ให้เพิ่มไปยัง count
        if (positiveFeedback === true) {
            addLikes();
        }

        //clear inputs
        resetForm()

        //add feedback to list
        addFeedback(newFeedback)
    }

    e.preventDefault()
}


function likeVideo() {
    likeIcon.classList.toggle('liked');

    if (likeIcon.classList.contains('liked')) {
        likeIcon.innerHTML = '<i class="fas fa-heart"></i>';
        // ตั้งค่า positiveFeedback เป็น true ในกรณีนี้
        positiveFeedback = true;
    } else {
        likeIcon.innerHTML = '<i class="far fa-heart"></i>';
        // ตั้งค่า positiveFeedback เป็น false ในกรณีนี้
        positiveFeedback = false;
    }
}


function addLikes(){
    likesCount++
    count.innerHTML = likesCount
}

function resetForm(){
    userName.value = ''
    comment.value = ''
    likeIcon.innerHTML ='<i class="far fa-heart"></i>'
    positiveFeedback = false
}

function addFeedback(item){
    //select fisrt letter of the user name
    const letter = (item.userName).charAt(0)
    //Create new div
    const div = document.createElement('div')
    //add class
    div.classList = 'comment__card'
    //add id
    div.id = 'item.id'
    // add html
    div.innerHTML=`
    <div class="pic center__display">
    ${letter}
    </div>
    <div class="comment__info">
        <small class="nickname">${item.userName}</small>
        <p class="comment">${item.userComment}</p>
        <div class="comment__bottom">
            <div class="heart__icon--comment">
                ${item.typeOfFeedback ? `<i class="fas fa-heart"></i>`:`<i class="far fa-heart"></i>`}
            </div>
            <button>Reply</button>
        </div>
    </div>
    `
    //insert feedback into the list
    commentCont.insertAdjacentElement('beforeend',div)
}