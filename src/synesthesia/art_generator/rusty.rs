// use std::cmp::Reverse;
// use std::collections::{BinaryHeap, HashMap};




// https://stackoverflow.com/questions/64262297/rust-how-to-find-n-th-most-frequent-element-in-a-collection

use std::cmp::{Eq, Ord, Reverse};
use std::collections::{BinaryHeap, HashMap};
use std::hash::Hash;

pub fn most_frequent<T>(array: &[T], k: usize) -> Vec<(usize, &T)>
where
    T: Hash + Eq + Ord,
{
    let mut map = HashMap::new();
    for x in array {
        *map.entry(x).or_default() += 1;
    }

    let mut heap = BinaryHeap::with_capacity(k + 1);
    for (x, count) in map.into_iter() {
        heap.push(Reverse((count, x)));
        if heap.len() > k {
            heap.pop();
        }
    }
    heap.into_sorted_vec().into_iter().map(|r| r.0).collect()
}


#[no_mangle]    
pub fn common(bars: &[&str], note_buf: *mut String)
{
    let mut i = 0;
    for bar in bars 
    {
        let result: String = most_frequent(&[bar][..], 1)[0].1.to_string();
        unsafe 
        {
            *note_buf.offset(i)  = result;
        }
        i += 1;
    }
}
