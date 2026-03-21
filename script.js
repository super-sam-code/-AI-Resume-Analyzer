async function analyze(){

console.log("Button clicked")

let fileInput = document.getElementById("resume")
let jobdesc = document.getElementById("jobdesc").value
let resultBox = document.getElementById("result")

if(fileInput.files.length === 0){
alert("Upload resume first")
return
}

let file = fileInput.files[0]

console.log("File:", file.name)
console.log("Job desc:", jobdesc)

let formData = new FormData()
formData.append("resume", file)
formData.append("job_description", jobdesc)

try{

console.log("Sending request...")

let res = await fetch("http://localhost:8000/analyze", {
method: "POST",
body: formData
})

console.log("Response received:", res)

let data = await res.json()

console.log("Data:", data)

resultBox.innerText = JSON.stringify(data, null, 2)

}catch(error){

console.log("ERROR:", error)
resultBox.innerText = "❌ Error connecting to backend"

}

let output = ""

output += "📊 Match Score: " + data.match_score + "%\n\n"

output += "-----------------------------\n"

output += "✅ Resume Skills:\n"
data.resume_skills.forEach(s => output += "• " + s + "\n")

output += "\n❌ Missing Skills:\n"
data.missing_skills.forEach(s => output += "• " + s + "\n")

output += "\n💡 Suggestions:\n"
data.suggestions.forEach(s => output += "• " + s + "\n")

resultBox.innerText = output
}