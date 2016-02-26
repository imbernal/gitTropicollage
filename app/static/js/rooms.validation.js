String.prototype.contains = function(it) { 
	return this.indexOf(it) != -1; 
};

Array.prototype.contains = function (val) {
	for (var i = 0; i < this.length; i++) {
		if (this[i] == val) {
			return true;
		}
	}
	return false;
}

$(function () {

	var simpleCount = $('#cantSimples');
	var doubleCount = $('#cantDobles');
	var tripleCount = $('#cantTriples');
	
	var cantHabitaciones	 = $('#cantHabitaciones option:selected').val() - '0';
	var sum = 0;

	$('#cantHabitaciones').on('change', function(){
      	cantHabitaciones = $(this).val();
  	});

	var inputs = $('#tab2 input[id*="cant"]');
	inputs.each(function (k, v) {
		var curr = $(v);
		var memory = [];
		
		curr.keyup(function (event_data) {
			var keyCode = event_data.keyCode;
			
			//TODO: Handle numeric pad as well
			//TODO: Apply jQuery validate instead of fancy colors that I'd applied.
			var keys_allowed = [8, 9, 37, 39, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57];	
			
			if(keys_allowed.contains(keyCode) && (keyCode != 8) && (keyCode != 37) && (keyCode != 39) && (keyCode != 9)) {
				var curr_value = parseInt(event_data.currentTarget.value);
				memory[$(this).attr('id')] = curr_value;

				sum = sum + curr_value;
				
				if (sum > cantHabitaciones)
					$(this).css({ 'border-color': 'red' });
				else
					$(this).css({ 'border-color': '#e5e5e5' });
				l(sum);
			}
			if (keyCode == 8) {
				sum = sum - parseInt(memory[$(this).attr('id')]);
				$(this).css({ 'border-color': '#e5e5e5' });
			}
		});
	});
});

function l(patt) {
	console.log(patt);
}