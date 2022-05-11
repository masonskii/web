window.onload = function () {

  const name = document.getElementById('name');
  const cardnumber = document.getElementById('cardnumber');
  const expirationdate = document.getElementById('expirationdate');
  const securitycode = document.getElementById('securitycode');
  const output = document.getElementById('output');
  const ccicon = document.getElementById('ccicon');
  const ccsingle = document.getElementById('ccsingle');
  const generatecard = document.getElementById('generatecard');


  let cctype = null;

  //Mask the Credit Card Number Input
  var cardnumber_mask = new IMask(cardnumber, {
    mask: [{
        mask: '9090 6940 0000 0000',
        regex: '^(5[1-5]\\d{0,2}|22[2-9]\\d{0,1}|2[3-7]\\d{0,2})\\d{0,12}',
        cardtype: 'fablab'
      },
      {
        mask: '0000 0000 0000 0000',
        cardtype: 'Unknown'
      }
    ],
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

  //Mask the Expiration Date
  var expirationdate_mask = new IMask(expirationdate, {
    mask: 'MM{/}YY',
    groups: {
      YY: new IMask.MaskedPattern.Group.Range([0, 99]),
      MM: new IMask.MaskedPattern.Group.Range([1, 12]),
    }
  });

  //Mask the security code
  var securitycode_mask = new IMask(securitycode, {
    mask: '000',
  });



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
    console.log(cardnumber_mask.masked.currentMask.cardtype);
    switch (cardnumber_mask.masked.currentMask.cardtype) {
      case 'american express':
        ccicon.innerHTML = amex;
        ccsingle.innerHTML = amex_single;
        swapColor('green');
        break;
      case 'visa':
        ccicon.innerHTML = visa;
        ccsingle.innerHTML = visa_single;
        swapColor('lime');
        break;
      case 'diners':
        ccicon.innerHTML = diners;
        ccsingle.innerHTML = diners_single;
        swapColor('orange');
        break;
      case 'discover':
        ccicon.innerHTML = discover;
        ccsingle.innerHTML = discover_single;
        swapColor('purple');
        break;
      case ('jcb' || 'jcb15'):
        ccicon.innerHTML = jcb;
        ccsingle.innerHTML = jcb_single;
        swapColor('red');
        break;
      case 'maestro':
        ccicon.innerHTML = maestro;
        ccsingle.innerHTML = maestro_single;
        swapColor('yellow');
        break;
      case 'mastercard':
        ccicon.innerHTML = mastercard;
        ccsingle.innerHTML = mastercard_single;
        swapColor('lightblue');

        break;
      case 'unionpay':
        ccicon.innerHTML = unionpay;
        ccsingle.innerHTML = unionpay_single;
        swapColor('cyan');
        break;
      default:
        ccicon.innerHTML = '';
        ccsingle.innerHTML = '';
        swapColor('grey');
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

  //On Input Change Events
  name.addEventListener('input', function () {
    if (name.value.length == 0) {
      document.getElementById('svgname').innerHTML = 'John Doe';
      document.getElementById('svgnameback').innerHTML = 'John Doe';
    } else {
      document.getElementById('svgname').innerHTML = this.value;
      document.getElementById('svgnameback').innerHTML = this.value;
    }
  });

  cardnumber_mask.on('accept', function () {
    if (cardnumber_mask.value.length == 0) {
      document.getElementById('svgnumber').innerHTML = '0123 4567 8910 1112';
    } else {
      document.getElementById('svgnumber').innerHTML = cardnumber_mask.value;
    }
  });

  expirationdate_mask.on('accept', function () {
    if (expirationdate_mask.value.length == 0) {
      document.getElementById('svgexpire').innerHTML = '01/23';
    } else {
      document.getElementById('svgexpire').innerHTML = expirationdate_mask.value;
    }
  });

  securitycode_mask.on('accept', function () {
    if (securitycode_mask.value.length == 0) {
      document.getElementById('svgsecurity').innerHTML = '985';
    } else {
      document.getElementById('svgsecurity').innerHTML = securitycode_mask.value;
    }
  });

  //On Focus Events
  name.addEventListener('focus', function () {
    document.querySelector('.creditcard').classList.remove('flipped');
  });

  cardnumber.addEventListener('focus', function () {
    document.querySelector('.creditcard').classList.remove('flipped');
  });

  expirationdate.addEventListener('focus', function () {
    document.querySelector('.creditcard').classList.remove('flipped');
  });

  securitycode.addEventListener('focus', function () {
    document.querySelector('.creditcard').classList.add('flipped');
  });
};