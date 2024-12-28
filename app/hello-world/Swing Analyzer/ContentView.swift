//
//  ContentView.swift
//  Swing Analyzer
//
//  Created by Nhan Tran on 12/26/24.
//

import SwiftUI

enum Emoji: String, CaseIterable {
    case 🤪
    case 😎
    case 😀
    case 😇
}


struct ContentView: View {
    
    @State var selection: Emoji = .😀
    
    var body: some View {
        NavigationView{
            VStack {
                Text(selection.rawValue)
                    .font(.system(size: 150))
                Picker("Select Emoji", selection: $selection){
                    ForEach(Emoji.allCases, id: \.self){ emoji in Text(emoji.rawValue)
                            .font(.system(size: 50))
                    }
                }
                .pickerStyle(.segmented)
            }
            .navigationTitle("Our first emoji picker!")
            .padding()

        }
    }
}

#Preview {
    ContentView()
}
