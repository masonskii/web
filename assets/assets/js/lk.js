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

  //Mask the Credit Card Number Input


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

$(document).ready(function() {


  const labels = document.querySelectorAll(".accordion-item__label");
  const tabs = document.querySelectorAll(".accordion-tab");

  function toggleShow() {
    const target = this;
    const item = target.classList.contains("accordion-tab")
      ? target
      : target.parentElement;
    const group = item.dataset.actabGroup;
    const id = item.dataset.actabId;

    tabs.forEach(function(tab) {
      if (tab.dataset.actabGroup === group) {
        if (tab.dataset.actabId === id) {
          tab.classList.add("accordion-active");
        } else {
          tab.classList.remove("accordion-active");
        }
      }
    });

    labels.forEach(function(label) {
      const tabItem = label.parentElement;

      if (tabItem.dataset.actabGroup === group) {
        if (tabItem.dataset.actabId === id) {
          tabItem.classList.add("accordion-active");
        } else {
          tabItem.classList.remove("accordion-active");
        }
      }
    });
  }

  labels.forEach(function(label) {
    label.addEventListener("click", toggleShow);
  });

  tabs.forEach(function(tab) {
    tab.addEventListener("click", toggleShow);
  });

});

$(function(){


        // collapse
        $("[data-collapse]").on("click", function(event){
          event.preventDefault();

          var $this = $(this),
          blocktId = $(this).data('collapse');

          $this.toggleClass("active");



        });
});
