fun check(exp: Boolean?, errMsg: String) {
    if (!exp!!) {
        System.out.println("Type failure: $errMsg")
    }
}
