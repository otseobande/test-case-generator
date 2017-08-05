Vue.filter('trim', (value)=>{
	return value.trim();
})

const app = new Vue({
	el: '#app',
	data: {
		processing: false,
		fileUploaded: false,
		fileError: false,
		fileName: "",
		umlStates: {},
	},
	methods:{
		uploadFile(event){
			let file = event.target.files[0];
			this.fileName = file.name;
			this.processing = true;

			let self = this;
			
			let panel_heading = document.querySelector("panel_heading")
			let panel_body = document.querySelector(".panel-body");

			if ((/\.xmi$/i).test(file.name)){

				let formData = new FormData();
				formData.set('file', file)

			    axios.post('upload_file', formData, {
			        headers: {
			          'Content-Type': 'multipart/form-data'
			        }
			    }).then((response)=>{
			    	if(response.statusText == "OK"){
			    		self.processing = false;
			    		self.umlStates = response.data;
			    		self.fileUploaded = true;	
			    	}
			    }).catch((err)=>{
			    	console.log(err);
			    });

			}else{
				this.processing = false;
				this.fileError = true;
			}
		}
	},
	computed:{
		path(){
			val = "";
			for (let i in this.umlStates){
				val += this.umlStates[i].name + "->"; 
			}
			return val;
		}
	},
	components:{
		alert: VueStrap.alert,
	}
});