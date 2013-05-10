$(document).ready(function() {
	var tactics = [];

	$("#btn_generate").click(function(event) {
		event.preventDefault();
		var dimensions = [];
		$('#form-dimensions select').each(function(idx, val) {
			var v = $(val).val();
			if (v == '忽略') {
				dimensions.push([]);
			} else if (v == '全部') {
				var all = [];
				$(this).children('option').slice(2).each(function(i, v) {
					all.push($(v).text());
				});
				dimensions.push(all);
			} else {
				dimensions.push([v]);
			}
		});
		console.log(dimensions);

		tactics = [];

		$.each(dimensions, function(idx, val) {
			if (val.length == 0) {
				if (tactics.length == 0) {
					tactics[0] = [""];
					return;
				}

				for ( i = 0; i < tactics.length; i++) {
					tactics[i].push("");
				}
				return;
			}

			if (tactics.length == 0) {
				for ( i = 0; i < val.length; i++) {
					tactics[i] = [val[i]];
				}
				return;
			}

			var new_tactics = [];
			for ( i = 0; i < val.length; i++) {
				for ( j = 0; j < tactics.length; j++) {
					tactics[j].push(val[i]);
					new_tactics.push(tactics[j].slice(0));
					tactics[j].pop();
				}
			}
			tactics = new_tactics;
		});

		console.log(tactics);

		var $body = $("#tbl_tactic tbody");
		$body.html("");
		$.each(tactics, function(idx, val) {
			var data = ['<tr>', '<td>' + (idx + 1) + '</td>'];
			for ( i = 0; i < val.length; i++) {
				data.push('<td>' + val[i] + '</td>');
			}
			data.push('</tr>');
			$body.append(data.join(''));
		});
	});
});
