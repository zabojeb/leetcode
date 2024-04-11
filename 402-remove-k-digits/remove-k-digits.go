func removeKdigits(num string, k int) string {
    stack := make([]byte, 0)

    for i := 0; i < len(num); i++ {
        digit := num[i]

        for k > 0 && len(stack) > 0 && stack[len(stack)-1] > digit {
            stack = stack[:len(stack)-1]
            k--
        }

        stack = append(stack, digit)
    }

    stack = stack[:len(stack)-k]

    var buffer bytes.Buffer
    leadingZero := true
    for _, digit := range stack {
        if leadingZero && digit == '0' {
            continue
        }
        leadingZero = false
        buffer.WriteByte(digit)
    }

    if buffer.Len() == 0 {
        return "0"
    }

    return buffer.String()
}