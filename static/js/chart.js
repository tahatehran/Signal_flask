function createChart(data) {
    const prices = data.map(coin => coin.quote.USD.price);
    const symbols = data.map(coin => coin.symbol);

    const trace = {
        x: symbols,
        y: prices,
        type: 'bar'
    };

    const layout = {
        title: 'Crypto Prices',
        xaxis: { title: 'Cryptocurrency' },
        yaxis: { title: 'Price (USD)' },
        responsive: true
    };

    Plotly.newPlot('chart', [trace], layout);
}
