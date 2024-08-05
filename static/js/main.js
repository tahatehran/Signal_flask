function updateData() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            createChart(data.data);
            updatePredictions(data.prediction);
            updateSignals(data.signals);
        });
}

function updatePredictions(prediction) {
    const predictionsDiv = document.getElementById('predictions');
    predictionsDiv.innerHTML = `<h2 class="text-2xl font-bold mb-4">Price Prediction</h2>
                                <p>Next price: $${prediction.toFixed(2)}</p>`;
}

function updateSignals(signals) {
    const signalsDiv = document.getElementById('signals');
    signalsDiv.innerHTML = '<h2 class="text-2xl font-bold mb-4">Trading Signals</h2>';
    signals.forEach(signal => {
        signalsDiv.innerHTML += `<p>${signal.symbol}: ${signal.signal}</p>`;
    });
}

// Update data every minute
setInterval(updateData, 60000);
updateData(); // Initial update
