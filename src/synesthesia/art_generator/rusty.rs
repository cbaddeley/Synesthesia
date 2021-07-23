
#[no_mangle]
pub fn note(freq: f64) -> i64
{
    let c0 = 440.0 * (2.0 as f64).powf(-4.75); 
    let h: f64 = (12.0 * (freq/c0).log2()).round();
    ((h as i64  % 12) as i64) * 1000 + (h as i64 / 12) as i64 // return the index of the notes and the octave as a decimal
}


// https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/