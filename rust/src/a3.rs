pub fn main() {
    let mut num :i64 = 600851475143;
    let mut fact = 2;
    while i64::pow(fact, 2) < num {
        if num % fact == 0 {
            num /= fact;
            fact =1;
        }
        fact +=1;
    }
    println!("{}",num);
}
