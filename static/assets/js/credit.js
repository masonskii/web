
window.onload = function () {
  const cardnumber = document.getElementById('cardnumber');
  const ccicon = document.getElementById('ccicon');
  const ccsingle = document.getElementById('ccsingle');


  let cctype = null;

  //Mask the Credit Card Number Input
  var cardnumber_mask = new IMask(cardnumber, {
    mask: [      {
        mask: '0000 0000 0000 0000',
        regex: '^(9090\\d{0,2}|6304|67\\d{0,2})\\d{0,12}',
        cardtype: 'fablab'
      },
      {
        mask: '0000 0000 0000 0000',
        cardtype: 'Unknown'
      }],
    dispatch: function (appended, dynamicMasked) {
      var number = (dynamicMasked.value + appended).replace(/\D/g, '');

      for (var i = 0; i < dynamicMasked.compiledMasks.length; i++) {
        let re = new RegExp(dynamicMasked.compiledMasks[i].regex);
        if (number.match(re) != null) {
          return dynamicMasked.compiledMasks[i];
        }
      }
    }
  });

let fablab ='';


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
  cardnumber_mask.on("accept", function () {
    switch (cardnumber_mask.masked.currentMask.cardtype) {
      case 'fablab':
        ccicon.innerHTML = fablab;
        ccsingle.innerHTML = fablab;
        swapColor('green');
        break;
      default:
        ccicon.innerHTML = '';
        ccsingle.innerHTML = '';
        swapColor('orange');
        break;
    }

  });





  // CREDIT CARD IMAGE JS
  document.querySelector('.preload').classList.remove('preload');
  document.querySelector('.creditcard').addEventListener('click', function () {
    if (this.classList.contains('flipped')) {
      this.classList.remove('flipped');
    } else {
      this.classList.add('flipped');
    }
  })


  cardnumber_mask.on('accept', function () {
    if (cardnumber_mask.value.length == 0) {
      document.getElementById('svgnumber').innerHTML = '0123 4567 8910 1112';
    } else {
      document.getElementById('svgnumber').innerHTML = cardnumber_mask.value;
    }
  });


  //On Focus Events
  name.addEventListener('focus', function () {
    document.querySelector('.creditcard').classList.remove('flipped');
  });

  cardnumber.addEventListener('focus', function () {
    document.querySelector('.creditcard').classList.remove('flipped');
  });

};

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