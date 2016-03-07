<html>

<head></head>

<body>

<h1> T1.p1: Chat de texto </h1>
<ul id="messages">

</ul>

<form action="/send" method=POST>
    <p> Nick <input name="nick" type="text" value="{{nick}}"/> </p>
    <p> Mensagem <input name="message" type="text" /> </p>
    <p> <input value="Enviar" type="submit" /> </p>
</form>

<script type="text/javascript" src="/static/jquery.js"></script>
<script type="text/javascript">
	$(function() {
		update()
	});

	function update() {
		$('#messages').load('/messages');

		window.setTimeout(update, 1000)
	}
</script>
</body>

</html>
