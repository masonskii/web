$('input[type=checkbox]').on('click', function ()  {
    if ( $(this).is(":checked") ) {
		$('.org-box').each(function(){
			$(this).css('display','block')
		})
		btn = document.querySelector('#button')
		btn.name = 'send_org'
	} else {
		$('.org-box').each(function(){
			$(this).css('display','none')
		})
		btn = document.querySelector('#button')
		btn.name = 'send_person'

	}
});