pub fn main() {
    let mut record = 1;
    for i in (100..1000).rev() {
        for j in (i..1000).rev() {
            let num = i*j;
            let snum = num.to_string();
            if snum == snum.chars().rev().collect::<String>() {
                if num > record {
                    record = num;
                }
            }
        }
    }
    println!("{}", record);
}
