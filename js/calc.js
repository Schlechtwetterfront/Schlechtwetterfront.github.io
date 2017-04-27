(function($) {

    var $flags = null
    var $flagInt = null
    var $flagHex = null

    var $renderTypeInt = null
    var $renderTypeHex = null

    var $data0Int = null
    var $data0Hex = null
    var $data1Int = null
    var $data1Hex = null

    var $chunk = null
    var $buildWithSpaces = null


    $(document).ready(function() {
        $flags = $('.flags')
        $flagInt = $('.flag-values #flag')
        $flagHex = $('.flag-values #flag-hex')

        $renderTypeInt = $('.render-type #render-type')
        $renderTypeHex = $('.render-type #render-type-hex')

        $data0Int = $('.data-values #data0')
        $data0Hex = $('.data-values #data0-hex')
        $data1Int = $('.data-values #data1')
        $data1Hex = $('.data-values #data1-hex')

        $chunk = $('.chunk #chunk')
        $buildWithSpaces = $('.chunk #build-with-spaces')

        bind($flagInt, $flagHex)
        bind($data0Int, $data0Hex)
        bind($data1Int, $data1Hex)

        $renderTypeInt.on('change', function() {
            var hex = parseInt($(this).val()).toString(16)
            $renderTypeHex.val(pad('00', hex, true))
        })

        $renderTypeHex.on('input change', function() {
            var int = parseInt($(this).val(), 16)
            $renderTypeInt.val(int)
        })

        $('#flags-to-values').on('click', function() {
            var val = 0
            $flags.find('input:checked').each(function() {
                val += parseInt($(this).data('val'))
            })
            $flagInt.val(val)
            $flagHex.val(pad('00', val.toString(16), true))
        })

        $('#values-to-flags').on('click', function() {
            var val = parseInt($flagInt.val())
            $flags.find('input').each(function() {
                if (val & parseInt($(this).data('val'))) {
                    $(this).prop('checked', true)
                } else {
                    $(this).prop('checked', false)
                }
            })
        })

        $('#build').on('click', function() {
            var chunk = '41 54 52 42 04 00 00 00 '
                        + $flagHex.val() + ' '
                        + $renderTypeHex.val() + ' '
                        + $data0Hex.val() + ' '
                        + $data1Hex.val()

            if (!$buildWithSpaces.prop('checked')) {
                chunk = chunk.replace(/ /g, '')
            }
            $chunk.val(chunk)
        })

        $('#from-chunk').on('click', function() {
            var chunk = $chunk.val()
            if (chunk.length > 24) {
                chunk = chunk.replace(/ /g, '')
            }

            var flag = chunk.substring(16, 18);
            var renderType = chunk.substring(18, 20);
            var data0 = chunk.substring(20, 22);
            var data1 = chunk.substring(22, 24);

            $flagHex.val(flag).change()
            $renderTypeHex.val(renderType).change()
            $data0Hex.val(data0).change()
            $data1Hex.val(data1).change()
            $('#values-to-flags').click()
        })

        $buildWithSpaces.on('change', function() {
            $('#build').click();
        })
    })

    function bind($intProvider, $hexProvider) {
        $intProvider.on('input change', function() {
            var hex = parseInt($(this).val()).toString(16)
            $hexProvider.val(pad('00', hex, true))
        })

        $hexProvider.on('input change', function() {
            var int = parseInt($(this).val(), 16)
            if (!isNaN(int)) {
                $intProvider.val(int)
            }
        })
    }

    function pad(pad, str, padLeft) {
        if (typeof str === 'undefined') 
            return pad;
        if (padLeft) {
            return (pad + str).slice(-pad.length);
        } else {
            return (str + pad).substring(0, pad.length);
        }
    }

})($)
