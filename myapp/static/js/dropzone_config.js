// dropzone config
Dropzone.options.imageDropzone = {
	paramName: "file",
	maxFilesize: 10,
  	addRemoveLinks: true,
  	acceptedFiles: 'image/*',
  	dictDefaultMessage: "",
	init: function() {
		dz = this;
	    this.on("success", function(file, response) {
	    	//alert('success')
	    	//console.log(file)
	    	//console.log(response)
	        //file.previewElement.id = response.id;
	        $(file.previewTemplate).find(".dz-details").append("<div class='dz-filename'><span id='dog'>Dog:"+response.dog*100+"%</span></div>");
	        $(file.previewTemplate).find(".dz-details").append("<div class='dz-filename'><span id='cat'>Cat:"+response.cat*100+"%</span></div>");
	        if (response.dog > response.cat){
	        	$(file.previewTemplate).find(".dz-details .dz-filename #dog").css("background-color","#f18973");
	        } else if (response.cat > response.dog){
	        	$(file.previewTemplate).find(".dz-details .dz-filename #cat").css("background-color","#f18973");
	        }
	        
	    });
	}
}