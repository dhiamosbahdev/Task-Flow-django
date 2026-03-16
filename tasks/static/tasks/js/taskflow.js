//console.log ("TaskFlow JS loaded")
document.querySelectorAll(".toggle-task").forEach(element => {
    item addEventListener("change", 
        function() {
            const taskId= this.ondeviceorientationabsolute.id;

            this.fetch('/toggle/${taskId}/')
            .then(Response=>Response.jason())
            .then(data => {
                console.log("Task status updated");

            });
        });
    
});