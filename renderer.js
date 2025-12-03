// DOM Elements
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');
const systemStatus = document.getElementById('systemStatus');
const threatCount = document.getElementById('threatCount');
const monitoringTime = document.getElementById('monitoringTime');
const logContainer = document.getElementById('logContainer');
const statusLight = document.querySelector('.status-light');

// State
let isMonitoring = false;
let threats = 0;
let startTime = null;
let timerInterval = null;

// Functions
function addLog(message, type = 'info') {
    const logEntry = document.createElement('p');
    logEntry.className = `log-entry ${type}`;
    const timestamp = new Date().toLocaleTimeString();
    logEntry.textContent = `[${timestamp}] ${message}`;
    logContainer.appendChild(logEntry);
    logContainer.scrollTop = logContainer.scrollHeight;
}

function updateTimer() {
    if (!startTime) return;
    
    const elapsed = Date.now() - startTime;
    const hours = Math.floor(elapsed / 3600000);
    const minutes = Math.floor((elapsed % 3600000) / 60000);
    const seconds = Math.floor((elapsed % 60000) / 1000);
    
    monitoringTime.textContent = 
        `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function startMonitoring() {
    isMonitoring = true;
    startTime = Date.now();
    
    startBtn.disabled = true;
    stopBtn.disabled = false;
    
    systemStatus.textContent = 'Active';
    statusLight.classList.add('active');
    
    addLog('Monitoring started', 'success');
    
    timerInterval = setInterval(updateTimer, 1000);
    
    // Simulate threat detection (for demo purposes)
    simulateThreatDetection();
}

function stopMonitoring() {
    isMonitoring = false;
    
    startBtn.disabled = false;
    stopBtn.disabled = true;
    
    systemStatus.textContent = 'Stopped';
    statusLight.classList.remove('active');
    
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
    
    addLog('Monitoring stopped', 'warning');
}

function resetSystem() {
    stopMonitoring();
    
    threats = 0;
    startTime = null;
    
    threatCount.textContent = '0';
    monitoringTime.textContent = '00:00:00';
    
    logContainer.innerHTML = '<p class="log-entry">System reset and ready...</p>';
    
    addLog('System reset completed', 'success');
}

function simulateThreatDetection() {
    if (!isMonitoring) return;
    
    // Randomly detect "threats" for demo purposes
    const nextDetection = Math.random() * 10000 + 5000; // 5-15 seconds
    
    setTimeout(() => {
        if (isMonitoring) {
            threats++;
            threatCount.textContent = threats;
            
            const threatTypes = [
                'Unidentified aerial object detected',
                'Suspicious flight pattern observed',
                'Unauthorized drone activity',
                'Low-flying aircraft detected',
                'Rapid altitude change detected'
            ];
            
            const randomThreat = threatTypes[Math.floor(Math.random() * threatTypes.length)];
            addLog(`⚠️ ALERT: ${randomThreat}`, 'error');
            
            simulateThreatDetection();
        }
    }, nextDetection);
}

// Event Listeners
startBtn.addEventListener('click', startMonitoring);
stopBtn.addEventListener('click', stopMonitoring);
resetBtn.addEventListener('click', resetSystem);

// Initialize
addLog('Application loaded successfully', 'success');
addLog('Click "Start Monitoring" to begin threat detection', 'info');
