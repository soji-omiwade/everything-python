! Note: this only works with the Intel Compiler
subroutine sqr(val)
    !DEC$ ATTRIBUTES DLLEXPORT, ALIAS:'sqr' :: sqr
    integer, intent(inout) :: val
    val = val ** 2
end subroutine sqr