let filesDone = 0
let filesToDo = 0
let progressBar = document.getElementById('progress-bar')

function initializeProgress(numfiles) {
  progressBar.value = 0
  filesDone = 0
  filesToDo = numfiles
}

function progressDone() {
  filesDone++
  progressBar.value = filesDone / filesToDo * 100
}
