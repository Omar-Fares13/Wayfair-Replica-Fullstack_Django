function openNav() {
    document.getElementById("mySidepanel").style.width = "576px";
  }
  
  function closeNav() {
    document.getElementById("mySidepanel").style.width = "0";
  }

  window.addEventListener('scroll', function() {
    var element = document.querySelector('.disappearing-element');
    if (window.scrollY > 40) {
        element.classList.add('disappear');
    } else {
        element.classList.remove('disappear');
    }
});

window.addEventListener('load', () => {
  const preloader = document.querySelector('.preloader');
  preloader.style.display = 'none';
});

window.addEventListener('scroll', () => {
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backToTopBtn.classList.add('show');
  } else {
    backToTopBtn.classList.remove('show');
  }
});

document.getElementById('backToTopBtn').addEventListener('click', () => {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
});

function changeImage(element) {

  var main_prodcut_image = document.getElementById('main_product_image');
  main_prodcut_image.src = element.src;
  

}