(function (path) {
	'use strict'
	var doRedirect = true

	var currentCounter = 0
	var timeToRedirect = 15
	var counterOnes = null
	var counterTens = null

	var counterIsActive = true

	var redirected = false

	var redirectTarget = '//schlechtwetterfront.net' + path

	window.onload = function() {
		counterOnes = document.querySelector('#countdown .counter.one')
		counterTens = document.querySelector('#countdown .counter.ten')

		var stopButton = document.querySelector('.stop-countdown')
		stopButton.onclick = function() {
			counterIsActive = false
		}

		currentCounter = timeToRedirect

		counterOnes.appendChild(newDigit(currentCounter % 10))
		counterTens.appendChild(newDigit(Math.floor(currentCounter / 10)))

		window.setInterval(update, 1000)
	}

	var update = function() {
		if (!counterIsActive) {
			return
		}

		var before = currentCounter
		currentCounter -= 1
		console.log(currentCounter)

		if (currentCounter < 0) {
			if (!redirected && doRedirect) {
				location = redirectTarget
				redirected = true
			}
			counterIsActive = false
		} else {
			var counter = null
			var newText = ''

			if (numDigits(before) == numDigits(currentCounter)) {
				scrollOver(counterOnes, currentCounter % 10)
			} else {
				scrollOver(counterTens, Math.floor(currentCounter / 10))
				scrollOver(counterOnes, currentCounter % 10)
			}
		}
	}

	var newDigit = function(text) {
		var digit = document.createElement('div')
		digit.appendChild(document.createTextNode(text))
		digit.className = 'digit current'
		return digit
	}

	var scrollOver = function(counter, newText) {
		// Clear previous element.
		var previous = counter.querySelector('.previous')
		if (previous) {
			counter.removeChild(previous)
		}

		// Add new element.
		counter.appendChild(newDigit(newText))
		
		// Mark element that is now the previous element.
		var digits = counter.querySelectorAll('.digit')
		if (digits.length > 1) {
			digits[0].className = 'digit previous'
		}
	}

	var numDigits = function(number) {
		return Math.max(Math.log(number) * Math.LOG10E + 1 | 0, 1)
	}
})(path)
