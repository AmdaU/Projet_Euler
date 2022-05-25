pub fn main(){
    let mut n1 = 1;
    let mut n2 = 2;
    let mut sum = 0;
    while n2 <= 4_000_000 {
        if n2 % 2 == 0 {
            sum+=n2;
        }
        let n3 = n1 + n2;
        n1 = n2;
        n2 = n3;
    }
    println!("{}", sum)
}
