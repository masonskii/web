
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}


window.onload = function () {
    const cardnumber = document.getElementById('cardnumber');
    const ccicon = document.getElementById('ccicon');
    const ccsingle = document.getElementById('ccsingle');


    let cctype = null;


    let fablab = '';


    //define the color swap function
    const swapColor = function (basecolor) {
        document.querySelectorAll('.lightcolor')
            .forEach(function (input) {
                input.setAttribute('class', '');
                input.setAttribute('class', 'lightcolor ' + basecolor);
            });
        document.querySelectorAll('.darkcolor')
            .forEach(function (input) {
                input.setAttribute('class', '');
                input.setAttribute('class', 'darkcolor ' + basecolor + 'dark');
            });
    };


    //pop in the appropriate card icon when detected

    // CREDIT CARD IMAGE JS
    document.querySelector('.creditcard').addEventListener('click', function () {
        if (this.classList.contains('flipped')) {
            this.classList.remove('flipped');
        } else {
            this.classList.add('flipped');
        }
    })
}

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

function openTab(evt, tab) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("content__inner");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tab");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	document.getElementById(tab).style.display = "block";
	evt.currentTarget.className += " active";
}

//Horizontal scroll for the tabs on mousewheel. If tabs are longer than the content section, there's a scroll bar but it's hidden to retain the design.
if (window.innerWidth > 800) {
	const scrollContainer = document.querySelector(".tabs");

	scrollContainer.addEventListener("wheel", (evt) => {
		evt.preventDefault();
		scrollContainer.scrollLeft += evt.deltaY;
	});
}


