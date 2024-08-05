function updateData() {
    fetch('/api/data')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                console.error('Error from server:', data.error);
                return;
            }
            createChart(data.data);
            updatePredictions(data.prediction);
            updateSignals(data.signals);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function updatePredictions(prediction) {
    const predictionsDiv = document.getElementById('predictions');
    if (prediction === null) {
        predictionsDiv.innerHTML = '<h2 class="text-2xl font-bold mb-4">Price Prediction</h2><p>Unable to make prediction at this time.</p>';
    } else {
        predictionsDiv.innerHTML = `<h2 class="text-2xl font-bold mb-4">Price Prediction</h2><p>Next price: $${prediction.toFixed(2)}</p>`;
    }
}

function updateSignals(signals) {
    const signalsDiv = document.getElementById('signals');
    if (signals === null || signals.length === 0) {
        signalsDiv.innerHTML = '<h2 class="text-2xl font-bold mb-4">Trading Signals</h2><p>No signals available at this time.</p>';
    } else {
        signalsDiv.innerHTML = '<h2 class="text-2xl font-bold mb-4">Trading Signals</h2>';
        signals.forEach(signal => {
            signalsDiv.innerHTML += `<p>${signal.symbol}: ${signal.signal}</p>`;
        });
    }
}

// Update data every minute
setInterval(updateData, 60000);
updateData(); // Initial update
