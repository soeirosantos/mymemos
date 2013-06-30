!function($) {
	$(function() {

	
		//submit for server.
		$('#btn-memorizar').on('click', function() {
			$.post('/', {
				'memo' : $('#memo').val()
			}, function() {
				alert('finish')
			});
		});
		
		

	})

}(window.jQuery)
