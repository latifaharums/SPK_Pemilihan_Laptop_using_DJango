function ngelink() {
    window.location='{% urls "checkin:cari" %}';
}

function NumFormatter (data) {
	return parseFloat(data).toLocaleString(undefined, {
		minimumFractionDigits: 2,
		maximumFractionDigits: 2
	});
}; 