<html>

<head></head>

<body>

<h1> T1.p1: Chat de texto <small id="status" style="font-size: 50%;">| <span style="color: lime;">Online</span></small></h1>
<ul id="messages">

</ul>

<form action="/send" method=POST>
    <p> Nick <input name="nick" type="text" value="{{nick}}"/> </p>
    <p> Mensagem <input name="message" type="text" /> </p>
    <p> <input value="Enviar" type="submit" /> </p>
</form>

<link rel="stylesheet" type="text/css" href="/static/style.css">
<script type="text/javascript" src="/static/jquery.js"></script>
<script type="text/javascript">
	$(function() {
		update()
	});

	var link = 1;
	function update() {
		$('#messages').load('/messages', function( response, status, xhr ) {
			if (status == 'error' && link) {
				link = 0;
				$('#status > span').css({color: 'red'}).text('Offline').addClass('blink_me');
				$('form input').attr('disabled', 'disabled');
			} else if (status != 'error' && !link) {
				link = 1;
				$('#status > span').css({color: 'green'}).text('Online').removeClass('blink_me');
				$('form input').removeAttr('disabled');
			}
		});

		window.setTimeout(update, 1000)
	}
</script>
</body>

</html>
