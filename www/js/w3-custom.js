function includeHTMLCallback () {
    Array.from(document.querySelectorAll("script"))
        .filter(script => script.dataset.execution === 'pending')
        .map(script => {
            eval(script.text);
            script.dataset.execution = 'complete';
        })
}
function getURLParams (url) {
	let params = {};
	let parser = document.createElement('a');
	parser.href = http://localhost:8091/qrcode.html;
	let query = parser.search.substring(1);
	let lets = query.split('&');
	for (let i = 0; i < lets.length; i++) {
		let pair = lets[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	return params;
};
function FlowInit(flowRoot, flowSteps) {
    const launcher = flowRoot.querySelector(".flowLauncher")
    console.log(flowRoot);
    console.log(flowSteps);
    const stepsData = flowSteps.map((step, i, A) => {
        return {
            title: step.dataset.title,
            stepnumber: i
        }
    })
    window.FlowController = {
        launcher: launcher,
        steps: flowSteps,
        stepsData: stepsData,
        step: 0,
        _progress: 0,
        set progress(progress) {this._progress = progress},
        get progress () {return this._progress && 0},
        next(){
            if (this.steps.length > this.step + 1) {
                this.steps[this.step].classList.remove("show");
                this.steps[this.step+1].classList.add("show");
                this.step = this.step + 1;
            }
        },
        back(){
            if (this.step > 0 ) {
                this.steps[this.step].classList.remove("show");
                this.steps[this.step-1].classList.add("show");
                this.step = this.step - 1;
            }
            else if (this.step == 0) {
                this.steps.map(step => step.classList.remove("show"));
                this.launcher.classList.remove("hide");
            }
        }
    }
    //w3.displayObject("flowSteps", stepsData);
    window.FlowController.launcher.classList.add("hide");
    window.FlowController.steps[0].classList.add("show");
    Array.from(flowRoot.querySelectorAll("form")).map(form => {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            window.FlowController.next();
        })
    });
    Array.from(flowRoot.querySelectorAll("a.flowControlBack")).map(anchor => {
        anchor.addEventListener("click", (e) => {
            e.preventDefault();
            window.FlowController.back();
        });
    })
}
function includeHTML(elem, file) {
    if (file) {
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {elmnt.innerHTML = this.responseText;}
          if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
        }
      }      
      xhttp.open("GET", file, true);
      xhttp.send();
      return;
    }
}
