var swiper = new Swiper('.blog-slider', {
      spaceBetween: 30,
      effect: 'fade',
      loop: true,
      mousewheel: {
        invert: false,
      },
      // autoHeight: true,
      pagination: {
        el: '.blog-slider__pagination',
        clickable: true,
      }
    });

const colors = ['#f5a147','#51cad8','#112b39'];
const numLines = 3;
var currCount = numLines;
const texts = document.querySelectorAll("#textClip text");
const blobs = document.querySelectorAll("#background path");

function colorBlobs() {
	blobs.forEach(blob => {
        blob.style.fill = colors[Math.floor(Math.random() * colors.length)];
    });
}

function nextIteration() {
	// Change the color of all the blobs
    colorBlobs();

    // Hide the old set of lines
    let startVal = currCount - numLines;
    if(startVal < 0) {
    	startVal = texts.length - numLines;
    }
    for(let i = startVal; i < startVal + numLines; i++) {
    	texts[i].style.display = "none";
    }
    // Show new set of lines
    for(let j = currCount; j < currCount + numLines; j++) {
    	texts[j].style.display = "inline";
    }
    currCount += numLines;
    if(currCount >= texts.length) {
    	currCount = 0;
    }
}

// Since all of our blobs are using the same animation, we only
// need to listen to one of them
blobs[0].addEventListener("animationiteration", nextIteration);

colorBlobs();

/*
let minSize=50,
el=document.querySelector('.under-head'),
page=document.querySelector('html'),
height={
  el:el.offsetHeight-minSize,
  page:500
}
document.addEventListener('scroll',()=>{
  let st=page.scrollTop
  if(st>=height.page) return
  let percent=height.page/st,
  value=height.el/percent
  el.style.height=height.el-value+minSize+'px'
})*/



$(function(){




   var header = $('#header'),
    intrH = $('#intro').innerHeight(),
    scrollOfSet =  $(window).scrollTop();

    //fiexd header
     checkscroll(scrollOfSet)

  $(window).on('scroll', function()  {

   scrollOfSet = $(this).scrollTop();

   checkscroll(scrollOfSet)
  });

  function checkscroll(scrollOfSet)
  {

    if (scrollOfSet >= intrH ) {
    	header.addClass('fixed');
    }   else
    {
    	header.removeClass('fixed');
    }
  }

   // smoot scroll
     $("[data-scroll]").on('click', function(event) {
       event.preventDefault();

       var $this = $(this),
          blocktId = $(this).data('scroll'),
          blockOfset = $(blocktId).offset().top;

         $('nav a').removeClass('active');
          $this.addClass('active');

          $("html , body").animate({
            scrollTop:blockOfset
          }, 500);



     });

     /*nav toogler*/
     $('#nav__toggle').on('click', function(event){
             event.preventDefault();
        $(this).toggleClass("active");
           $('#nav').toggleClass("active");


     });


});