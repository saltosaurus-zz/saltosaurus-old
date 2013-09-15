jQuery(document).ready ->
	$(".add-comment").click (e) ->
		e.preventDefault()
		$( this ).remove()
		comment = $( this ).parent().parent().find(".newComment")
		comment.find("input[type=text], textarea").val("")
		comment.slideDown()
		
		comment.find("#newComment").click (e) ->
			e.preventDefault()
			$.ajax {
				type: "POST"
				url: "newComment"
				data: $("form").serialize()
				success: ->
					comment.slideUp()
					numCom = $("#numComm")
					numCom.fadeOut( ->
						numCom.text(parseInt(numCom.text()) + 1)
						)
					numCom.fadeIn()
				}
				
	$("article").find("#newComment").click (e) ->
		e.preventDefault()
		form = $("form")
		$.ajax {
				type: "POST"
				url: "../newComment"
				data: form.serialize()
				success: ->
					author = form.find("input[type=text]").val()
					comment = form.find("textarea").val()
					element = $('<article>', { class: "comment", style: "display: none;" }).append($('<h1>'+author+'</h1>')).append($('<p>'+comment+'</p>'))
					$(".comments").prepend(element)
					$(".comment").slideDown()
					$(".newComment").slideUp()
				}
		