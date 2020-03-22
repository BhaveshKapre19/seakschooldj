$(document).ready(function() {
	console.log("Js Loaded");
	// $('#AddNoticeButton').click(function(){
	// 	$('#Add_Notice').trigger('click');
	// });

	var Url = location.pathname.split('/');
	if (Url[4]=='Update') {
		var valueofImage = $("#div_id_teacherImage a").attr("href");
		$('#ImageTeacher').attr("src",valueofImage);
	}

})













